#!/usr/bin/env python

import os
import acefile
from fame.core.module import ProcessingModule
from fame.common.utils import tempdir


class ACE_Extract(ProcessingModule):
    name = "ace-extract"
    description = "Extract disguised ace archives"
    acts_on = None

    def is_susp_ace(self, target):
        arch_ext = ['.rar', '.zip', '.arj']
        return target[-4:].lower() in arch_ext and acefile.is_acefile(target)

    def extract(self, target):
        os.chdir(tempdir())
        with acefile.open(target) as arch:
            arch.extractall()
            return arch.getnames()

    def each(self, target):
        if self.is_susp_ace(target):
            self.add_tag('ACE_disguised')
            files = self.extract(target)
            for f in files:
                self.add_extracted_file(f)
