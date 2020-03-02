from kazoo.client import KazooClient
import os
import click
import yaml
import time

ZK_URI = os.getenv('ZOOKEEPER_URL', '127.0.0.1:2181')
ZK_PREFIX = '/amalgam/'

try:
    zk = KazooClient(hosts=ZK_URI, read_only=True)
    zk.start()
except Exception as e:
    click.echo(str(e))
    exit(1)

@click.group()
def cli():
    pass

@click.command()
@click.option('--filename', default='../deployment/dev.yaml', help='Filename to load to sentry-zookeeper')
def load(filename):
    global zk
    with open(filename,'r') as f:
        output = f.read()
        content = yaml.load(output, Loader=yaml.FullLoader)
        for i in content['default_context']:
            key = ZK_PREFIX + i
            value = content['default_context'][i]
            zk.ensure_path(key)
            zk.set(key, value.encode('utf-8'))
        click.echo(f'Loaded {filename}')
        zk.stop()

@click.command()
@click.argument('key')
def list(key):
    global zk
    key = ZK_PREFIX + key
    s = zk.get_children(key)
    click.echo(f'list key {s}')

@click.command()
@click.argument('key')
@click.argument('value')
def set(key, value):
    global zk
    key = ZK_PREFIX + key
    zk.ensure_path(key)
    zk.set(key, value.encode('utf-8'))
    zk.stop()

@click.command()
@click.argument('key')
@click.option('--get-version/--no-version', default=False)
def get(key, get_version):
    global zk
    key = ZK_PREFIX + key
    try:
        if zk.exists(key):
            data, stat = zk.get(key)
            if get_version:
                click.echo("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
            else:
                click.echo(data.decode("utf-8"))
        else:
            click.echo("Key does not exists")
    except Exception as e:
        click.echo(str(e))
    finally:
        zk.stop()

@click.command()
@click.argument('key')
@click.option('--recursive/--no-recursive', default=False)
def delete(key, recursive):
    global zk
    key = ZK_PREFIX + key
    try:
        if zk.exists(key):
            zk.delete(key, recursive=recursive)
        else:
            click.echo("Key does not exists")
    except Exception as e:
        click.echo(str(e))
    finally:
        zk.stop()

@click.command()
@click.argument('key')
@click.option('--recursive/--no-recursive', default=False)
def watch(key, recursive):
    global zk
    key = ZK_PREFIX + key
    try:
        if zk.exists(key):
            @zk.DataWatch(key)
            def watch_node(data, stat):
                print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
            while(True):
                try:
                    time.sleep(1)
                except KeyboardInterrupt:
                    stored_exception=sys.exc_info()
        else:
            click.echo("Key does not exists")
    except Exception as e:
        click.echo(str(e))
    finally:
        zk.stop()

cli.add_command(load)
cli.add_command(list)
cli.add_command(get)
cli.add_command(set)
cli.add_command(delete)
cli.add_command(watch)
