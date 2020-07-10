#!/usr/bin/python3
from Service.StoriaTakeShobo import StoriaTakeShobo
from Service.ComicTrail import ComicTrail
from Service.ComicWalker import ComicWalker
from Service.ComicDays import ComicDays

from Service.Solver.PtImgSolver import PtImgSolver
from Service.Solver.XorSolver import XorSolver
from Service.Solver.SlideSolver import SlideSolver

from Storage.FolderStorage import FolderStorage
from Storage.ZipStorage import ZipStorage

import argparse
import os

#TO-DO clean this up, expand args, move services container elsewhere, and so on.. 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='downloads manga chapters')
    parser.add_argument('--download')
    parser.add_argument('-o', default="folder")
    parser.add_argument('path')
    args = parser.parse_args()

    services = [
        ComicTrail(PtImgSolver()),
        StoriaTakeShobo(PtImgSolver()),
        ComicWalker(XorSolver()),
        ComicDays(SlideSolver())
    ]

    storage_options = {
        "folder":   lambda path: FolderStorage(path),
        "zip":      lambda path: ZipStorage(path)
    }

    if args.download:
        storage = storage_options.get(args.o)(args.path)
        for service in services:
            if service.supports_url(args.download):
                print("Found matching service for requested chapter url")
                service.download(args.download, storage)
                print('Downloaded chapter to ' + os.path.abspath(args.path))
            