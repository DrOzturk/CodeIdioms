# Luigi Example

This is just a simple 'Hello World' example to demonstrate the use of Luigi.

It will create a file that says "Hello", another that says "World", and concatenate the contents of those files into a third that says "Hello World". 

Usage:

```
pipenv install
pipenv shell
# start as bg process, at defautl port:
luigid --background --logdir=logs
# otherwise occupies shell
# luigid --port=8082 --logdir=logs
# and you can ctrl-c to kill
python hello_world.py HelloWorldTask --id=some_id
```
go and see results at default port:
http://localhost:8082

To kill the background service:
```bash
ps -ef | grep -i luigid
```
see process id
then
```bash
kill -9 $process_id
```