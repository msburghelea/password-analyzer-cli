import argparse
import analyzer
import generate

parser = argparse.ArgumentParser(description='Password Analyzer.')
subparsers = parser.add_subparsers(dest='command', help='Type of analyzer to use.')
analyze_parser = subparsers.add_parser('analyze', help='Analyze a password.')
analyze_parser.add_argument('password', type=str, help='The password to analyze.')
analyze_parser.add_argument("--check", action="store_true", help="Enable HIBP lookup")
generate_parser = subparsers.add_parser('generate', help='Generate a secure password.')
generate_parser.add_argument('--length', type=int, default=12, help='Length of the generated password (default: 12).')
args = parser.parse_args()
if args.command is None:
    parser.print_help()
elif args.command == 'analyze':
    result = analyzer.analyze(args.password, check=args.check)
    analyzer.print_results(result)
elif args.command == 'generate':
    print("Generating a secure password...")
    password = generate.generate_password(args.length)
