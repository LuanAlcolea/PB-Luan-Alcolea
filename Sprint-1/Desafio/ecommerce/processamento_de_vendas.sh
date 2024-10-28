#!/bin/bash

echo --- Processamento de Vendas ---

cd /home/Sprint-01/ecommerce

echo --- Criar diretorios ---
mkdir -p vendas/backup

echo --- Copiar arquivos e aplicar data---
cp dados_de_vendas.csv vendas

cp vendas/dados_de_vendas.csv vendas/backup/backup-dados-$(date +"%Y%m%d").csv
arquivo="vendas/backup/backup-dados-$(date +"%Y%m%d").csv"

echo --- Gerar relatorio ---

numero=$(ls vendas/backup/relatorio-*.txt 2>/dev/null | sed -e "s|^vendas/backup/relatorio-||" -e 's|\.txt$||' | sort -n | tail -1)


if [ -z "$numero" ]; then
   numero=0
fi

proximo_numero=$((numero+1))

relatorio="vendas/backup/relatorio-${proximo_numero}.txt"

touch "$relatorio"

echo "--- Relatorio $proximo_numero ---" >> $relatorio

echo "Data do sistema: $(date '+%Y/%m/%d %H:%M')" >> $relatorio

echo "Data do primeiro registro de venda: $(head -2 dados_de_vendas.csv | tail -1 | cut -d ',' -f 5)" >> $relatorio

echo "Data do ultimo registro de venda: $(tail -1 dados_de_vendas.csv | cut -d ',' -f 5)" >> $relatorio

echo "Quantidade total de itens vendidos: $(cut -d ',' -f 2 dados_de_vendas.csv | tail -n +2 | sort | uniq | wc -l)" >> $relatorio

echo "" >> $relatorio

echo "Primeiras 10 linhas do arquivo: dados_de_vendas.csv " >> $relatorio
head -10 dados_de_vendas.csv >> $relatorio

echo "" >> $relatorio

echo --- Compactando backup-dados-yyyymmdd ---
zip "$arquivo.zip" "$arquivo"

echo --- Removendo arquivos ---
rm vendas/dados_de_vendas.csv
rm $arquivo

echo ""
