import os
import magic
from fame.core.module import ProcessingModule
from fame.common.utils import tempdir


class ACE_Extract(ProcessingModule):
    name = "ace-extract"
    description = "Extract disguised ace archives"

    def is_susp_ace(self, target):
        arch_ext = ['.rar', '.zip', '.arj']
        return target[-4:].lower() in arch_ext and magic.from_file(target).startswith('ACE')

    def extract(self, target):
        tmpdir = tempdir()
        os.system("acefile-unace -d {} -x {}".format(tmpdir, target))
        files = os.popen("acefile-unace -l {}".format(target)).read().split('\n')
        for i in range(len(files)):
            files[i] = tmpdir + '/' + files[i]
        return files

    def each(self, target):
        if self.is_susp_ace(target):
            self.add_tag('ACE_disguised')
            files = self.extract(target)
            for f in files:
                if os.path.isfile(f):
                    self.add_extracted_file(f)
            return True
