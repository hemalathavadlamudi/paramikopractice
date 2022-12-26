import logging
import os
import logging as log
log.basicConfig(filename='result.log')


log.info('start the execution')
if os.path.exists("data"):
    log.warning('directory already exists')
else:
    os.mkdir('hema')
    log.info('created directory')
log.critical('serious issue')
log.error('another error')
log.info('close the program')
log.warning('exit the program')




