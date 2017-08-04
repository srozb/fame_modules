import os
from fame.core.module import ProcessingModule
from fame.common.utils import tempdir


class JSE_Decode(ProcessingModule):
    name = "jse-decode"
    description = "Decode JScript.Encoded file"

    def each(self, target):
        if not target.lower().endswith('.jse'):
            return False
        tmpdir = tempdir()
        dest_file = "{}/{}".format(tmpdir, target[:-1])
        os.system('fame/modules/srozb/processing/decoder {} {}'.format(
            target, dest_file))
        self.add_extracted_file(dest_file)
        return True
