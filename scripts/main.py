import argparse
from classes.Generate import Generate
from classes.Cleanup import Cleanup

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode',type=str, dest='mode',required=True,choices=['cleanup','generate'])
    parser.add_argument('-a', '--amount',type=int, dest='amount_of_secret_holders',required=False,choices=range(1,9))
    parser.add_argument('-q', '--quota', type=int, dest='decryption_quota', choices=range(1,101),required=False)
    args = parser.parse_args()
    
    if args.mode == 'cleanup':
        cleanup = Cleanup()
        exit()
        
    if args.mode == 'generate':
        generate = Generate(args.amount_of_secret_holders, args.decryption_quota)
        generate.execute()
        exit()