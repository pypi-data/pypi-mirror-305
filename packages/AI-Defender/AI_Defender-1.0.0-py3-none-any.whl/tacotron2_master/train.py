import sys
import os
import argparse
import torch
import time
import math
from numpy import finfo
import torch.distributed as dist
from torch.utils.data import DataLoader
from torch.utils.data.distributed import DistributedSampler
from torch.cuda.amp import autocast, GradScaler
from torch.optim.lr_scheduler import ReduceLROnPlateau

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Adjusting path to include the current directory
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Importing modules from the current directory
from model import Tacotron2
from utils_custom import dynamic_range_compression, dynamic_range_decompression, window_sumsquare, to_gpu, get_mask_from_lengths
from data_utils import TextMelLoader, TextMelCollate
from loss_function import Tacotron2Loss
from logger import Tacotron2Logger
from distributed import apply_gradient_allreduce
from text_processing import text_to_sequence
from hparams import create_hparams  # Assuming hparams.py is in the same directory

# Constants
# Define the HParams class
class HParams:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

# Define the create_hparams function
def create_hparams(hparams_string=None):
    """Create model hyperparameters."""
    hparams = HParams(
        epochs=100,
        batch_size=32,
        learning_rate=0.001,
        grad_clip_thresh=1.0,
        weight_decay=1e-6,
        n_frames_per_step=1,
        n_mel_channels=80,
        prenet_dim=256,
        attention_rnn_dim=1024,
        attention_dim=128,
        decoder_rnn_dim=1024,
        attention_location_n_filters=32,
        attention_location_kernel_size=31,
        postnet_n_convolutions=5,
        postnet_embedding_dim=512,
        encoder_n_convolutions=3,
        encoder_embedding_dim=512,
        encoder_kernel_size=5,
        cudnn_enabled=True,
        cudnn_benchmark=False,
        fp16_run=False,
        use_saved_learning_rate=False,
        dynamic_loss_scaling=True,
        distributed_run=False,
        seed=1234,
        training_files='./train_data.txt',
        validation_files='./val_data.txt',
        mask_padding=True,
        n_symbols=148,
        symbols_embedding_dim=512,
        max_decoder_steps=1000,
        gate_threshold=0.5,
        p_attention_dropout=0.1,
        p_decoder_dropout=0.1,
        postnet_kernel_size=5,
        max_wav_value=32768.0,
        text_cleaners=['english_cleaners'],
        sampling_rate=22050,
        load_mel_from_disk=False,
        mel_fmin=0.0,
        mel_fmax=8000.0,
        n_fft=1024,
        hop_length=256,
        win_length=1024,
        filter_length=1024,  # Added `filter_length` to match `n_fft`
        clip_gradients=True,
        dropout_rate=0.5,
        mask_decoder=True,
        power=1.5,
        ref_level_db=20,
        max_abs_value=4.0,
        min_level_db=-100,
        signal_normalization=True,
        symmetric_mels=True,
        max_norm=1.0,
        allow_clipping_in_normalization=True,
        clip_mels_length=True,
        use_lws=False,
        silence_threshold=2,
        lower_bound_decay=0.1,
        preemphasize=True,
        preemphasis=0.97,
        all_in_one=True,
        contrast_factor=1.0,
        pitch_shift=0,
        speed_factor=1.0,
        noise_shaping=True,
        noise_reduction_level=0.1,
        data_split_ratio=0.9,
        lr_decay_factor=0.5,
        early_stopping=True,
        patience=10,
        attention_heads=4,
        model_variant="original",
        encoder_type="rnn",
        decoder_type="gru",
        rnn_layers=3,
        lstm_hidden_units=512,
        gru_bidirectional=True,
        attention_window=7,
        max_grad_norm=5.0,
        use_l2_regularization=True,
        regularization_factor=1e-5,
        adam_beta1=0.9,
        adam_beta2=0.999,
        learning_rate_decay_start=5000,
        learning_rate_decay_end=50000,
        fine_tuning=False,
        pre_trained_model_path="path/to/pretrained/model",
        vocoder="griffin-lim",
        use_stft_loss=True,
        stft_loss_weight=1.0,
        style_embedding_dim=128,
        residual_connection=True,
        variance_adaptor=True,
        multi_speaker=True,
        speaker_embedding_dim=256,
        multi_language=False,
        language_embedding_dim=128,
        speaker_adversarial_training=False,
        use_weight_norm=True,
        use_batch_norm=False,
        drop_frame_rate=0.1,
        compute_overrun=False,
        max_mel_frames=900,
        reduction_factor=1,
        token_positional_encoding=True,
        position_max_length=1000,
        normalize_before=True,
        use_postnet=True,
        guided_attention=True,
        guided_attention_weight=100.0,
        mask_pos=False,
        text_encoder="phoneme",
        use_spk=False,
        spk_dim=512,
        latent_dim=128,
        posterior_encoder=True,
        external_speaker_embedding=False,
        model_checkpoint="checkpoint.pth",
        max_duration=300,
        min_duration=20,
        vocoder_sample_rate=22050,
        hop_size=256,
        num_mels=80,
        decoder_prenet_dropout=0.5,
        encoder_prenet_dropout=0.5,
        pitch_predictor_dropout=0.2,
        energy_predictor_dropout=0.2,
        use_ctc_loss=True,
        ctc_weight=0.5,
        normalize_mel=True,
        use_denoiser=True,
        training_noise_reduction=False,
        learning_rate_schedule="exponential",
        pitch_control=1.0,
        energy_control=1.0,
        mel_scaling_factor=1.0,
        gradient_accumulation_steps=1,
        max_epoch=500,
        num_attention_heads=8,
        use_speaker_embedding=False,
        speaker_embedding_path="",
        fp16_opt_level="O1",
        use_dynamic_loss_scaling=False,
        batch_first=True,
        truncate_length=800,
        use_alignment=True,
        attention_rnn_type="LSTM",
        duration_predictor_layers=2,
        duration_predictor_kernel_size=3,
        duration_predictor_dropout=0.1,
        freeze_encoder=False,
        pre_trained_encoder_path="",
        text_embedding_dim=128,
        filter_size=3,
        use_multihead_attention=False,
        encoder_attention_dropout=0.2,
        decoder_attention_dropout=0.3,
        encoder_conv_layers=5,
        decoder_conv_layers=3,
        use_positionwise_feed_forward=True,
        use_relative_positions=False,
        encoder_decoder_attention_heads=4,
        sampling_temperature=1.0,
        use_glow_tts=False,
        use_gate_prediction=True,
        gate_loss_weight=1.0,
        max_text_length=300,
        max_audio_length=500000,
        trainable_layers="all",
        base_model_lr=1e-4,
        train_vocoder_separately=False,
        use_weight_decay=True,
        weight_decay_start_step=10000,
        weight_decay_end_step=20000,
        checkpoint_interval=1000,
        logging_interval=100,
        grad_accumulation_steps=1,
        batch_size_validation=16,
        alignment_layer="conv",
        alignment_kernel_size=3,
        embed_scale=1.0,
        training_type="mixed",
        input_mean_normalization=True,
        input_var_normalization=True,
        freeze_pretrained_model=False,
        use_adaptive_learning_rate=True,
        encoder_dropout=0.1,
        decoder_dropout=0.2,
        stft_hop_length=256,
        stft_window_size=1024,
        use_mask=True,
        mask_threshold=0.5,
        encoder_attention_type="global",
        decoder_attention_type="local",
        use_decoder_state_for_attention=True,
        initial_learning_rate=0.0005,
        fine_tuning_learning_rate=0.0001,
        encoder_scale=0.5,
        decoder_scale=1.0,
        spk_adversarial_training=False,
        grad_clip_type="global_norm",
        init_gain=0.02,
        lstm_dropout=0.3,
        pitch_max=500.0,
        pitch_min=50.0,
        energy_max=600.0,
        energy_min=20.0,
        stop_at_epoch=200,
        minibatch_size=16,
        align_with_attention_loss=False,
        attention_score_mask_value=-1e9,
        model_ema_decay=0.999,
        multi_head_key_value_dim=64,
        multi_head_query_dim=64,
        wavernn=False,
        speaker_encoder_path="",
        decoder_rnn_layers=2,
        use_framewise_energy=True,
        adjust_learning_rate=True,
        evaluation_mode=False,
        run_on_gpu=True,
        distributed_backend="nccl",
        optimizer_type="adam",
        save_interval_epochs=5,
        validate_interval_epochs=2
    )
    
    return hparams

# Function to parse hparams from a string and update the hparams object
def parse_hparams_string(hparams_string, hparams):
    if hparams_string:
        for kv in hparams_string.split(","):
            key, value = kv.split("=")
            # Ensure the correct type is set based on existing hparams
            setattr(hparams, key, type(getattr(hparams, key))(value))

# Ensure GPU is detected
print(torch.cuda.is_available())  # Should print 'True' if GPU is detected

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Function definitions like reduce_tensor, init_distributed, prepare_dataloaders, etc.

def reduce_tensor(tensor, n_gpus):
    rt = tensor.clone()
    dist.all_reduce(rt, op=dist.ReduceOp.SUM)
    rt /= n_gpus
    return rt

def init_distributed(hparams, n_gpus, rank, group_name):
    assert torch.cuda.is_available(), "Distributed mode requires CUDA."
    print("Initializing Distributed")
    torch.cuda.set_device(rank % torch.cuda.device_count())
    dist.init_process_group(
        backend=hparams.dist_backend, init_method=hparams.dist_url,
        world_size=n_gpus, rank=rank, group_name=group_name)
    print("Done initializing distributed")

def prepare_dataloaders(hparams):
    trainset = TextMelLoader(hparams.training_files, hparams)
    valset = TextMelLoader(hparams.validation_files, hparams)
    collate_fn = TextMelCollate(hparams.n_frames_per_step)

    if hparams.distributed_run:
        train_sampler = DistributedSampler(trainset)
        shuffle = False
    else:
        train_sampler = None
        shuffle = True

    train_loader = DataLoader(trainset, num_workers=1, shuffle=shuffle,
                              sampler=train_sampler,
                              batch_size=hparams.batch_size,
                              pin_memory=False,
                              drop_last=True, collate_fn=collate_fn)
    return train_loader, valset, collate_fn

def prepare_directories_and_logger(output_directory, log_directory, rank):
    print(f"Output Directory: {output_directory}")
    print(f"Log Directory: {log_directory}")
    
    if output_directory is None or log_directory is None:
        raise ValueError("Output or Log directory is not provided.")
    
    if rank == 0:
        if not os.path.isdir(output_directory):
            os.makedirs(output_directory)
            os.chmod(output_directory, 0o775)
        if not os.path.isdir(log_directory):
            os.makedirs(log_directory)
            os.chmod(log_directory, 0o775)
        logger = Tacotron2Logger(os.path.join(output_directory, log_directory))
    else:
        logger = None
    return logger

def load_model(hparams, device):
    model = Tacotron2(hparams).to(device)
    if hparams.fp16_run:
        model.decoder.attention_layer.score_mask_value = finfo('float16').min
    if hparams.distributed_run:
        model = apply_gradient_allreduce(model)
    return model

def warm_start_model(checkpoint_path, model, ignore_layers):
    assert os.path.isfile(checkpoint_path)
    print(f"Warm starting model from checkpoint '{checkpoint_path}'")
    checkpoint_dict = torch.load(checkpoint_path, map_location='cpu')
    model_dict = checkpoint_dict['state_dict']
    if len(ignore_layers) > 0:
        model_dict = {k: v for k, v in model_dict.items() if k not in ignore_layers}
        dummy_dict = model.state_dict()
        dummy_dict.update(model_dict)
        model_dict = dummy_dict
    model.load_state_dict(model_dict)
    return model

def load_checkpoint(checkpoint_path, model, optimizer):
    assert os.path.isfile(checkpoint_path)
    print(f"Loading checkpoint '{checkpoint_path}'")
    checkpoint_dict = torch.load(checkpoint_path, map_location='cpu')
    model.load_state_dict(checkpoint_dict['state_dict'])
    optimizer.load_state_dict(checkpoint_dict['optimizer'])
    learning_rate = checkpoint_dict['learning_rate']
    iteration = checkpoint_dict['iteration']
    print(f"Loaded checkpoint '{checkpoint_path}' from iteration {iteration}")
    return model, optimizer, learning_rate, iteration

def save_checkpoint(model, optimizer, learning_rate, iteration, filepath):
    print(f"Saving model and optimizer state at iteration {iteration} to {filepath}")
    torch.save({'iteration': iteration,
                'state_dict': model.state_dict(),
                'optimizer': optimizer.state_dict(),
                'learning_rate': learning_rate}, filepath)

def validate(model, criterion, valset, iteration, batch_size, n_gpus,
             collate_fn, logger, distributed_run, rank):
    model.eval()
    with torch.no_grad():
        val_sampler = DistributedSampler(valset) if distributed_run else None
        val_loader = DataLoader(valset, sampler=val_sampler, num_workers=1,
                                shuffle=False, batch_size=batch_size,
                                pin_memory=False, collate_fn=collate_fn)
        val_loss = 0.0
        for i, batch in enumerate(val_loader):
            x, y = model.parse_batch(batch)
            y_pred = model(x)
            loss = criterion(y_pred, y)
            if distributed_run:
                reduced_val_loss = reduce_tensor(loss.data, n_gpus).item()
            else:
                reduced_val_loss = loss.item()
            val_loss += reduced_val_loss
        val_loss = val_loss / (i + 1)
    model.train()
    if rank == 0:
        print(f"Validation loss {iteration}: {val_loss:.9f}")
        logger.log_validation(val_loss, model, y, y_pred, iteration)

def train(output_directory, log_directory, checkpoint_path, warm_start, n_gpus, rank, group_name, hparams):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    if hparams.distributed_run:
        init_distributed(hparams, n_gpus, rank, group_name)
    
    torch.manual_seed(hparams.seed)
    torch.cuda.manual_seed(hparams.seed)
    
    model = load_model(hparams, device)

    learning_rate = hparams.learning_rate
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, weight_decay=hparams.weight_decay)

    if hparams.fp16_run:
        from apex import amp
        model, optimizer = amp.initialize(model, optimizer, opt_level='O2')

    criterion = Tacotron2Loss()
    logger = prepare_directories_and_logger(output_directory, log_directory, rank)
    train_loader, valset, collate_fn = prepare_dataloaders(hparams)

    iteration = 0
    epoch_offset = 0
    if checkpoint_path is not None:
        if warm_start:
            model = warm_start_model(checkpoint_path, model, hparams.ignore_layers)
        else:
            model, optimizer, _learning_rate, iteration = load_checkpoint(checkpoint_path, model, optimizer)
            if hparams.use_saved_learning_rate:
                learning_rate = _learning_rate
            iteration += 1
            epoch_offset = max(0, int(iteration / len(train_loader)))

    model.train()
    is_overflow = False
    for epoch in range(epoch_offset, hparams.epochs):
        print(f"Epoch: {epoch}")
        for i, batch in enumerate(train_loader):
            start = time.perf_counter()
            for param_group in optimizer.param_groups:
                param_group['lr'] = learning_rate
            model.zero_grad()
            x, y = model.parse_batch(batch)
            y_pred = model(x)
            loss = criterion(y_pred, y)
            if hparams.distributed_run:
                reduced_loss = reduce_tensor(loss.data, n_gpus).item()
            else:
                reduced_loss = loss.item()
            if hparams.fp16_run:
                with amp.scale_loss(loss, optimizer) as scaled_loss:
                    scaled_loss.backward()
            else:
                loss.backward()

            if hparams.fp16_run:
                grad_norm = torch.nn.utils.clip_grad_norm_(amp.master_params(optimizer), hparams.grad_clip_thresh)
                is_overflow = math.isnan(grad_norm)
            else:
                grad_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), hparams.grad_clip_thresh)

            optimizer.step()
            if not is_overflow and rank == 0:
                duration = time.perf_counter() - start
                print(f"Train loss {iteration} {reduced_loss:.6f} Grad Norm {grad_norm:.6f} {duration:.2f}s/it")
                logger.log_training(reduced_loss, grad_norm, learning_rate, duration, iteration)
            if not is_overflow and (iteration % hparams.iters_per_checkpoint == 0):
                validate(model, criterion, valset, iteration, hparams.batch_size, n_gpus, collate_fn, logger, hparams.distributed_run, rank)
                if rank == 0:
                    checkpoint_path = os.path.join(output_directory, f"checkpoint_{iteration}")
                    save_checkpoint(model, optimizer, learning_rate, iteration, checkpoint_path)
            iteration += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filelist', type=str, help='Path to the file list', required=True)
    parser.add_argument('-o', '--output_directory', type=str, help='Directory to save checkpoints', required=True)
    parser.add_argument('-c', '--config_file', type=str, help='Path to the config file', required=True)
    parser.add_argument('-l', '--log_directory', type=str, help='Directory to save tensorboard logs', required=False)
    parser.add_argument('--checkpoint_path', type=str, default=None, required=False, help='Checkpoint path')
    parser.add_argument('--warm_start', action='store_true', help='Load model weights only, ignore specified layers')
    parser.add_argument('--n_gpus', type=int, default=1, required=False, help='Number of gpus')
    parser.add_argument('--rank', type=int, default=0, required=False, help='Rank of current gpu')
    parser.add_argument('--group_name', type=str, default='group_name', required=False, help='Distributed group name')
    parser.add_argument('--hparams', type=str, required=False, help='Comma separated name=value pairs')
    args = parser.parse_args()
    
    # Create hyperparameters
    # Hyperparameters
    hparams = create_hparams()
    if args.hparams:
        parse_hparams_string(args.hparams, hparams)
    hparams.training_files = args.filelist
    hparams.validation_files = "tacotron2_master/val_data.txt"
    
    # Debugging Print Statements
    print(f"Using file list: {args.filelist}")
    print(f"Output directory: {args.output_directory}")
    print(f"Log directory: {args.log_directory}")
    print(f"Config file: {args.config_file}")
    print("Final Hyperparameters:")
    for key, value in vars(hparams).items():
        print(f"{key}: {value}")

    # Create necessary directories if they do not exist
    if not os.path.exists(args.output_directory):
        os.makedirs(args.output_directory)
    if args.log_directory and not os.path.exists(args.log_directory):
        os.makedirs(args.log_directory)

    # Call the train function with the parsed arguments
    train(args.output_directory, args.log_directory, args.checkpoint_path, args.warm_start, args.n_gpus, args.rank, args.group_name, hparams)

    # Load dataset
    audiopaths_and_text = "filelist.txt"  # Path to filelist containing audio paths and texts
    text_mel_loader = TextMelLoader(audiopaths_and_text, hparams)
    # Instantiate the model
    model = Tacotron2(hparams)