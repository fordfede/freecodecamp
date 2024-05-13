CREATE SCHEMA datamarts;

CREATE TABLE datamarts.stock_foto_dia_anterior AS
SELECT
    sf.idStock,
    sf.Descrip,
    sf.Apto,
    sf.Usuario,
    sf.Terminal,
    sf.TS,
    s.CantStock,
    s.Unidades,
    s.Scanning
FROM
    StockFisico sf
JOIN
    Stocks s ON sf.idStock = s.IdStock
JOIN
    hub_stock hs ON sf.idStock = hs.IdStock
WHERE
    DATE(sf.TS) = DATEADD(day, -1, CURRENT_DATE);

CREATE TABLE datamarts.proveedores AS
SELECT
    ha.idarticulo,
    ha.Mna,
    ta.Descrip,
    ta.TipoCotizacion,
    ta.Usuario,
    ta.Terminal,
    ta.Ts
FROM
    hub_art ha
JOIN
    sat_type ta ON ha.Mna = ta.Mna;

CREATE TABLE datamarts.scanning_productos AS
SELECT
    s.Id,
    a.idarticulo,
    a.Mna,
    a.SectSecc,
    a.CodigoSap,
    s.Scanning,
    s.CantStock,
    s.Unidades,
    s.Usuario,
    s.Terminal,
    s.Ts
FROM
    Stocks s
JOIN
    Articulos a ON s.Id = a.id
JOIN
    hub_stock hs ON s.IdStock = hs.IdStock
JOIN
    hub_art ha ON a.idarticulo = ha.idarticulo;
