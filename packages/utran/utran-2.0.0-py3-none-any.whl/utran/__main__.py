import os
import sys



if __name__ == "__main__":
    try:
        import utran
    except ImportError:
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        import utran
        
    utran.Cli.cli()
