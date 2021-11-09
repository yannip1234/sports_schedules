#!/bin/zsh
docker-compose -H "ssh://yanni@10.0.4.213" -f docker-compose.prod.yml down && docker-compose -H "ssh://yanni@10.0.4.213" -f docker-compose.prod.yml up -d --build --force-recreate