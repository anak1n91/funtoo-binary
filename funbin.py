#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from urllib2 import urlopen

class color:
    Red = '\033[91m'
    Blue = '\033[94m'
    Yellow = '\033[93m'
    Bold = '\033[1m'
    End = '\033[0m'

subprocess.call(['clear'])
print '%sAutomate creation of isolated build environment for building binaries for Funtoo Linux%s.' % (color.Bold, color.End)

print '%sYou need to have your kernel config ready.%s' % (color.Bold, color.End)

print '%sChecking if you are root...%s' % (color.Bold, color.End)
if os.geteuid() != 0:
    print '%s%sFunbin needs to be run as root, sorry! Quitting...%s' % (color.Bold, color.Red, color.End)
    sys.exit('%sPlease re-run as root%s' % (color.Bold, color.End))
else:
    print '%sYou are root, continuing!%s' % (color.Bold, color.End)

stage86athlon = 'http://build.funtoo.org/funtoo-current/x86-32bit/athlon-xp/stage3-latest.tar.xz'
stage86generic = 'http://build.funtoo.org/funtoo-current/x86-32bit/generic_32/stage3-latest.tar.xz'
stage86i686 ='http://build.funtoo.org/funtoo-current/x86-32bit/i686/stage3-latest.tar.xz'
stage86pentium = 'http://build.funtoo.org/funtoo-current/x86-32bit/pentium4/stage3-latest.tar.xz'

stage64bulldozer = 'http://build.funtoo.org/funtoo-current/x86-64bit/amd64-bulldozer/stage3-latest.tar.xz'
stage64k10 = 'http://build.funtoo.org/funtoo-current/x86-64bit/amd64-k10/stage3-latest.tar.xz'
stage64k8 = 'http://build.funtoo.org/funtoo-current/x86-64bit/amd64-k8/stage3-latest.tar.xz'
stage64piledriver = 'http://build.funtoo.org/funtoo-current/x86-64bit/amd64-piledriver/stage3-latest.tar.xz'
stage64steamroller = 'http://build.funtoo.org/funtoo-current/x86-64bit/amd64-steamroller/stage3-latest.tar.xz'
stage64core2 = 'http://build.funtoo.org/funtoo-current/x86-64bit/core2_64/stage3-latest.tar.xz'
stage64corei7 = 'http://build.funtoo.org/funtoo-current/x86-64bit/corei7/stage3-latest.tar.xz'
stage64generic = 'http://build.funtoo.org/funtoo-current/x86-64bit/generic_64/stage3-latest.tar.xz'
stage64haswell = 'http://build.funtoo.org/funtoo-current/x86-64bit/intel64-haswell/stage3-latest.tar.xz'
stage64ivybridge = 'http://build.funtoo.org/funtoo-current/x86-64bit/intel64-ivybridge/stage3-latest.tar.xz'


def stages(stage):
    file_name = stage.split('/')[-1]
    resp = urlopen(stage)
    f = open(file_name, 'wb')
    meta = resp.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print 'Downloading: %s Bytes: %s' % (file_name, file_size)
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = resp.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()
    print ' '

dir = raw_input('%sPath to base environment directory: [%s/root/env/laptop-32bit%s%s]: %s' % (color.Bold, color.Blue, color.End, color.Bold, color.End))

def env():
    subprocess.call(['install', '-d', dir])
    print '%sChanging directories to: %s%s' % (color.Bold, color.End, dir)
    subprocess.call(['sleep', '1'])
    os.chdir(dir)
    print '%sSuccessfully changed directories to:%s %s' % (color.Bold, color.End, dir)
    subprocess.call(['sleep', '1'])

def tarball():
    print '%sArchitecture is 64bit or 32bit.%s' % (color.Bold, color.End)
    print '%s%sMicroarchiecture for 32bit are: %s' % (color.Bold, color.Blue, color.End)
    print 'athlon-xp'
    print 'generic'
    print 'i686'
    print 'pentium'
    print '-----------------------------------------------------'
    print '%s%sMicroarchitectures for 64bit are: %s' % (color.Bold, color.Blue, color.End)
    print 'bulldozer'
    print 'k10'
    print 'k8'
    print 'piledriver'
    print 'steamroller'
    print 'core2'
    print 'corei7'
    print 'generic'
    print 'haswell'
    print 'ivybridge'
    print '-----------------------------------------------------'
    print '%sPlease consult http://www.funtoo.org/Subarches to find more information on what microarchitecture you should use.' % color.Bold
    print 'State your answer as "arch microarch" so the script will pull the right stage'
    print 'Example: 64bit corei7%s' % color.End
    print '-----------------------------------------------------'
    print '%s%sThe arch and microarch needs to match your target machine, if you use a 64bit corei7 stage3 on your target machine, you must use a 64bit corei7 stage3 to build the packages.%s' % (color.Bold, color.Red, color.End)
    print '-----------------------------------------------------'
    raw_input('%sPlease press enter to continue%s' % (color.Bold, color.End))
    stage = raw_input('%sWhat is your architecture and microarchitecture?%s ' % (color.Bold, color.End))
    if stage == '64bit corei7':
        stages(stage64corei7)
    elif stage == '64bit bulldozer':
        stages(stage64bulldozer)
    elif stage == '64bit k10':
        stages(stage64k10)
    elif stage == '64bit k8':
        stages(stage64k8)
    elif stage == '64bit piledriver':
        stages(stage64piledriver)
    elif stage == '64bit steamroller':
        stages(stage64steamroller)
    elif stage == '64bit core2':
        stages(stage64core2)
    elif stage == '64bit generic':
        stages(stage64generic)
    elif stage == '64bit haswell':
        stages(stage64haswell)
    elif stage == '64bit ivybridge':
        stages(stage64ivybridge)
    elif stage == '32bit athlon-xp':
        stages(stage86athlon)
    elif stage == '32bit generic':
        stages(stage86generic)
    elif stage == '32bit i686':
        stages(stage86i686)
    elif stage == '32bit pentium':
        stages(stage86pentium)
    else:
        print '%sYou need to choose an architecture and microarchitecture in the format:%s $ARCH $MICROARCH' % (color.Bold, color.End)
        print '%sExample:%s 64bit corei7' % (color.Bold, color.End)
        sys.exit('Please re-run funbin')

def chroot():
    print '%sPreparing to untar stage3 and chroot into:%s %s (This can take some time...)' % (color.Bold, color.End, dir)
    subprocess.call(['tar', '-xJpf', 'stage3-latest.tar.xz'])
    subprocess.call(['mount', '--bind', '/sys', 'sys'])
    subprocess.call(['mount', '--bind', '/proc', 'proc'])
    subprocess.call(['mount', '--bind', '/dev', 'dev'])
    subprocess.call(['cp', '/etc/resolv.conf', 'etc'])
    kernel = raw_input('%sPath to your kernel config: ex: [%s/root/files/kernel.config%s%s] %s' % (color.Bold, color.Blue, color.End, color.Bold, color.End))
    subprocess.call(['cp', kernel, '%s/config' % dir])
    os.chroot(dir)
    print '%sSyncing Funtoo Portage tree...%s' % (color.Bold, color.End)
    subprocess.call(['emerge', '--sync'])
    os.system('echo \'EMERGE_DEFAULT_OPTS="--quiet-build=y --autounmask=n"\' >> /etc/portage/make.conf')
    os.system('echo \'FEATURES="buildpkg"\' >> /etc/portage/make.conf')
    proc = raw_input('%sHow many cores in your processor?%s ' % (color.Bold, color.End))
    os.system('echo \'MAKE_OPTS="%s"\' >> /etc/portage/make.conf' % proc)
    sources = raw_input('%sWhat kernel sources does your target machine have? [vanilla-sources/gentoo-sources]%s ' % (color.Bold, color.End))
    subprocess.call(['emerge', sources])
    subprocess.call(['mv', '/config', '/usr/src/linux'])
    print '%sBuilding kernel...%s' % (color.Bold, color.End)
    os.chdir('/usr/src/linux')
    subprocess.call(['make', 'silentoldconfig'])
    subprocess.call(['make'])
    subprocess.call(['make', 'modules_install'])
    print '%sFinished...%s' % (color.Bold, color.End)
    print '%sEnvironment is ready for use!%s' % (color.Bold, color.End)

def script():
    script = raw_input('%sWould you like to create a script to take user input to build packages for you?%s ' % (color.Bold, color.End))
    if script == 'yes':
        print '%sCreating script...%s' % (color.Bold, color.End) # placeholder more than anything
    elif script == 'no':
        print '%sNot creating script%s' % (color.Bold, color.End)
        print '%sYou will need to manually chroot into your environment at %s and build the packages you would like%s' % (color.Bold, dir, color.End)
    else:
        print '%sDefaulting to not creating script.%s' % (color.Bold, color.End)
        print '%sYou will need to manually chroot into your environment at "%s" and build the packages you would like%s' % (color.Bold, dir, color.End)

def run():
    env()
    tarball()
    chroot()
    script()
    subprocess.call(['umount', '%s/proc' % dir])
    subprocess.call(['umount', '%s/sys' % dir])
    subprocess.call(['umount', '%s/dev' % dir])

try:
    if __name__ == '__main__':
        run()
    else:
        sys.exit()
except (KeyboardInterrupt):
    print ' '
    sys.exit(1)