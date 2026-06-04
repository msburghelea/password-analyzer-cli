import argparse
import analyzer
import generate

parser = argparse.ArgumentParser(description='Analizador de contraseñas.')
subparsers = parser.add_subparsers(dest='comando', help='Tipo de analizador a utilizar.')
analyze_parser = subparsers.add_parser('analyze', help='Analizar una contraseña.')
analyze_parser.add_argument('password', type=str, help='La contraseña a analizar.')
analyze_parser.add_argument("--check", action="store_true", help="Activa la consulta a HIBP")
generate_parser = subparsers.add_parser('generate', help='Generar una contraseña segura.')
generate_parser.add_argument('--length', type=int, default=12, help='Longitud de la contraseña generada (por defecto: 12).')
args = parser.parse_args()
if args.comando is None:
    parser.print_help()
elif args.comando == 'analyze':
    resultado = analyzer.analizar(args.password, check=args.check)
    analyzer.imprimir_resultados(resultado)
elif args.comando == 'generate':
    print("Generando una contraseña segura...")
    generate.generar_contrasena(args.length)
