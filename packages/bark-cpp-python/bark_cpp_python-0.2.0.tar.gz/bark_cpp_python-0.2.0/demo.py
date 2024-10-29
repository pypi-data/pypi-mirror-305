import argparse

from bark_cpp import Bark


print(
"""
                \033[93m ___       _      ___     __  ___\033[0m
 /\__/\  woof   \033[93m|    \    / \    |    \  |  |/  /\033[0m
/      \  woof  \033[93m|    /   /   \   |    /  |     /\033[0m
\      /        \033[93m|    \  /  _  \  |  _ \  |     \\\033[0m
 \____/         \033[93m|____/ /__/ \__\ |_| |_\ |__|\__\\\033[0m
    
"""
)

def parse_arguments():
    """Parses command-line arguments for the Bark model."""
    parser = argparse.ArgumentParser(description="Run the Bark audio generation model.")

    parser.add_argument("model_path", type=str,
                        help="Path to the Bark model file.")
    parser.add_argument("-p", "--prompt", type=str,
                        help="Prompt for the audio generation.")
    parser.add_argument("--temp", type=float, default=0.7,
                        help="Temperature for sampling (text and coarse encoders).")
    parser.add_argument("--fine_temp", type=float, default=0.5,
                        help="Temperature for sampling (fine encoder).")
    parser.add_argument("--min_eos_p", type=float, default=0.2,
                        help="Minimum probability for EOS token (text encoder).")
    parser.add_argument("-w", "--sliding_window_size", type=int, default=60,
                        help="Sliding window size for coarse encoder.")
    parser.add_argument("--max_coarse_history", type=int, default=630,
                        help="Maximum history for coarse encoder.")
    parser.add_argument("-s", "--sample_rate", type=int, default=24000,
                        help="Sample rate of the generated audio.")
    parser.add_argument("-b", "--target_bandwidth", type=int, default=6,
                        help="Target bandwidth (kbps) for the audio codec.")
    parser.add_argument("-n", "--n_steps_text_encoder", type=int, default=768,
                        help="Maximum number of semantic tokens to generate.")
    parser.add_argument("--semantic_rate_hz", type=float, default=49.9,
                        help="Semantic frequency rate.")
    parser.add_argument("--coarse_rate_hz", type=float, default=75.0,
                        help="Coarse frequency rate.")
    parser.add_argument("--seed", type=int, default=0,
                        help="Random seed for initialization.")
    parser.add_argument("-t", "--threads", type=int, default=1,
                        help="Number of threads to evaluate.")
    parser.add_argument("--dest", type=str, required=False, default=None,
                        help="Path to save the generated audio.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    bark = Bark(
        model_path=args.model_path,
        temp=args.temp,
        fine_temp=args.fine_temp,
        min_eos_p=args.min_eos_p,
        sliding_window_size=args.sliding_window_size,
        max_coarse_history=args.max_coarse_history,
        sample_rate=args.sample_rate,
        target_bandwidth=args.target_bandwidth,
        n_steps_text_encoder=args.n_steps_text_encoder,
        semantic_rate_hz=args.semantic_rate_hz,
        coarse_rate_hz=args.coarse_rate_hz,
        seed=args.seed
    )
    audio_arr = bark.generate_audio(args.prompt, args.threads)

    print("Evaluated time: {:.2f}s".format(bark.get_eval_time() / 1e6))
    if args.dest:
        bark.write_wav(args.dest, audio_arr)