-- E01
select cod, titulo, autor, editora, valor, publicacao, edicao, idioma
from livro
where publicacao > '2015-01-01'
order by cod

-- E02
select titulo, valor
from livro
order by valor desc
limit 10

-- E03
SELECT  COUNT(l.cod) AS quantidade, ed.nome, en.estado, en.cidade
FROM editora ed
INNER JOIN livro l ON ed.codEditora = l.editora
INNER JOIN endereco en ON ed.endereco = en.codEndereco
GROUP BY ed.codEditora, ed.nome, en.estado, en.cidade
ORDER BY quantidade DESC
LIMIT 5

-- E04
SELECT a.nome, a.codAutor, a.nascimento, count(l.cod) AS quantidade
FROM autor a
LEFT JOIN livro l on a.codAutor = l.autor 
GROUP BY a.codAutor, a.nascimento
ORDER BY a.nome ASC

-- E05
SELECT DISTINCT a.nome
FROM autor a
JOIN livro l on a.codAutor = l.autor
JOIN editora ed on l.editora = ed.codEditora 
JOIN endereco en on ed.endereco = en.codEndereco
WHERE en.estado NOT IN ("RIO GRANDE DO SUL","SANTA CATARINA","PARANÁ")
ORDER BY a.nome ASC

-- E06
SELECT a.codAutor, a.nome, COUNT(l.cod) AS quantidade_publicacoes
FROM autor a
LEFT JOIN livro l ON a.codAutor = l.autor
GROUP BY a.codAutor, a.nome
ORDER BY quantidade_publicacoes DESC
LIMIT 1

-- E07
SELECT a.nome
FROM autor a
LEFT JOIN livro l ON a.codAutor = l.autor
GROUP BY a.codAutor, a.nome
HAVING COUNT(l.cod) < 1
ORDER BY a.nome ASC