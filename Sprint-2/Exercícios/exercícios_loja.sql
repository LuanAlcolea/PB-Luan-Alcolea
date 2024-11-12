-- E08
select vendedor.cdvdd, vendedor.nmvdd
from TBVENDEDOR as vendedor
left join TBVENDAS as vendas
on vendedor.cdvdd = vendas.cdvdd
where vendas.status = "Concluído"
group by vendedor.cdvdd, vendedor.nmvdd
order by sum(vendas.qtd) desc
limit 1

-- E09
select cdpro, nmpro
from TBVENDAS
where dtven between '2014-02-03' and '2018-02-02'
and status = "Concluído"
group by cdpro, nmpro
order by sum(qtd) desc
limit 1

-- E10
select vendedor.nmvdd as vendedor,
round(sum(vendas.qtd * vendas.vrunt), 2) as valor_total_vendas,
round(sum(vendas.qtd * vendas.vrunt) * (vendedor.perccomissao) / 100, 2) as comissao
from TBVENDEDOR as vendedor
left join TBVENDAS as vendas
on vendedor.cdvdd = vendas.cdvdd
and vendas.status = "Concluído"
group by vendedor.nmvdd
order by comissao DESC

-- E11
select cdcli, nmcli,
sum(vendas.qtd * vendas.vrunt) as gasto
from TBVENDAS as vendas
where status = 'Concluído'
group by cdcli, nmcli
order by gasto desc
limit 1

-- E12
select dependente.cddep, dependente.nmdep, dependente.dtnasc,
sum(vendas.qtd * vendas.vrunt) as valor_total_vendas
from TBVENDEDOR as vendedor
join TBDEPENDENTE as dependente on vendedor.cdvdd = dependente.cdvdd
join TBVENDAS as vendas on vendas.cdvdd = vendedor.cdvdd
where vendas.status = "Concluído"
group by dependente.cddep
order by valor_total_vendas asc
limit 1

-- E13
select vendas.cdpro, vendas.nmcanalvendas, vendas.nmpro,
sum(vendas.qtd) as quantidade_vendas
from TBVENDAS as vendas
where vendas.status = "Concluído"
group by vendas.cdpro, vendas.nmcanalvendas, vendas.nmpro
order by quantidade_vendas asc
limit 10

-- E14
select vendas.estado,
round(avg(vendas.qtd * vendas.vrunt),2) as gastomedio
from TBVENDAS as vendas
where vendas.status = "Concluído"
group by vendas.estado
order by gastomedio DESC

-- E15
select vendas.cdven
from TBVENDAS as vendas
where vendas.deletado = 1
group by vendas.cdven
order by vendas.cdven ASC

-- E16
select vendas.estado, vendas.nmpro,
round(avg(vendas.qtd), 4) as quantidade_media
from TBVENDAS as vendas
where vendas.status = "Concluído"
group by vendas.estado, vendas.nmpro
order by vendas.estado, vendas.nmpro