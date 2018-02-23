# testing using processes with Python!!!


open_proc = subprocess.Popen( 'ls -l')
less_proc = subprocess.Popen('less')

# do error checking here
with open_proc, less_proc: 
    pass


class CheckedPopen(subprocess.Popen):
    def wait(self):
        if super().wait() != 0:
            raise subprocess.CalledProcessError(self.returncode, self.args)
        return self.returncode
