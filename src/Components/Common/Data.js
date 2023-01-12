import React from "react";
import JsonData from "../../assets/data/data.json";

function Data() {
  const data = [...JsonData].sort((a, b) => (a.nLojas > b.nLojas ? -1 : 1));
  const DisplayData = data.map((data, index) => {
    return (
      <tr key={index}>
        <td id="loja" className="voweIMG">
          <a
            href={"https://www.google.com/search?q=" + data.nome}
            target="_blank"
            rel="noreferrer"
          >
            <img src={data.img} alt={data.nome} className="rounded"></img>
          </a>
        </td>
        <td id="livelo" className="vowe">
          <a href={data.url.livelo} target="_blank" rel="noreferrer">
            {data.valor.livelo}
          </a>
        </td>
        <td id="smiles" className="vowe">
          <a href={data.url.smiles} target="_blank" rel="noreferrer">
            {data.valor.smiles}
          </a>
        </td>
        <td id="curteai" className="vowe">
          <a href={data.url.curteai} target="_blank" rel="noreferrer">
            {data.valor.curteai}
          </a>
        </td>
        <td id="latampass" className="vowe">
          <a href={data.url.latampass} target="_blank" rel="noreferrer">
            {data.valor.latampass}
          </a>
        </td>
        <td id="esfera" className="vowe">
          <a href={data.url.esfera} target="_blank" rel="noreferrer">
            {data.valor.esfera}
          </a>
        </td>
      </tr>
    );
  });

  return (
    <div className="table-responsive table-card mt-3 mb-1">
      <table className="table align-middle table-nowrap" id="customerTable">
        <thead className="table-light">
          <tr>
            <th className="sort text-center leng" data-sort="Loja">
              Loja
            </th>
            <th className="sort text-center leng" data-sort="Livelo">
              Livelo
            </th>
            <th className="sort text-center leng" data-sort="Smiles">
              Smiles
            </th>
            <th className="sort text-center leng" data-sort="Curtai">
              Curtai
            </th>
            <th className="sort text-center leng" data-sort="LatamPass">
              LatamPass
            </th>
            <th className="sort text-center leng" data-sort="Esfera">
              Esfera
            </th>
          </tr>
        </thead>
        <tbody className="list form-check-all text-center">{DisplayData}</tbody>
      </table>
    </div>
  );
}

export default Data;
