#!/bin/bash

echo "---Consolidador de processamento de vendas---"

relatorio=vendas/backup/relatorio
relatoriofinal=${relatorio}-final.txt

echo "--- Consolidador de processamento de vendas ---" >> $relatoriofinal

echo "" >> $relatoriofinal

cat ${relatorio}-1.txt ${relatorio}-2.txt ${relatorio}-3.txt ${relatorio}-4.txt >> $relatoriofinal
