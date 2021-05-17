#!/usr/bin/env python3

import click
import boto3

@click.command(help="This code does label detecttion")
@click.option('--file', prompt='I need your name of file in the bucket!',
              help='This is the name of the file')
def detect(file):
    client = boto3.client('rekognition')

    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'mingfu',
                'Name': file,
            },
        },
    )
    click.echo(click.style(f"Detecting labels for {file}:", fg="red"))
    labels = response['Labels']
    for label in labels:
        name = label['Name']
        confidence = label['Confidence']
        click.echo(click.style(f"{name}: {confidence}", fg="green"))
        #print(f"{name}: {confidence}")
        
        
if __name__ == '__main__':
    # pylint: disable=E1120
    detect()