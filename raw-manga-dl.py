from Service.StoriaTakeShobo import StoriaTakeShobo
from Service.ComicTrail import ComicTrail
from Service.Solver.PtImgSolver import PtImgSolver
from Storage.FolderStorage import FolderStorage
from Storage.ZipStorage import ZipStorage
import argparse
import os

#Testing purposes only
#TO-DO clean this up, expand args, move services container elsewhere, and so on.. 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='downloads manga chapters')
    parser.add_argument('--download')
    parser.add_argument('path')
    args = parser.parse_args()
    solver = PtImgSolver()
    services = [
        ComicTrail(solver),
        StoriaTakeShobo(solver)
    ]
    if args.download:
        storage = FolderStorage(args.path)
        for service in services:
            if service.supports_url(args.download):
                print("Found matching service for requested chapter url")
                service.download(args.download, storage)
                print('Downloaded chapter to ' + os.path.abspath(args.path))