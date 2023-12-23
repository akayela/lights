#!/bin/bash
cd ~/ && 
ngrok http 8000 --domain=witty-frog-previously.ngrok-free.app --basic-auth 'admin:admin/15'

