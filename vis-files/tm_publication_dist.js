d3.csv('/nbextensions/distribution_per_publication.csv').then(data => {
  const cols = data.columns.slice(2);
  const colors = cols.map((item, index) => {
    d3.interpolateTurbo((index + 1) / cols.length);
  });
  const {
    BarChart,
    Bar,
    Label,
    Cell,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend
  } = Recharts;
  ReactDOM.render( React.createElement(BarChart, {
    width: 400,
    height: 200,
    data: data,
    margin: {
      top: 30,
      right: 30,
      left: 20,
      bottom: 10
    }
  }, React.createElement(CartesianGrid, {
    strokeDasharray: "3 3"
  }), React.createElement(XAxis, {
    dataKey: "publication_name"
  }), React.createElement(YAxis, null), React.createElement(Tooltip, null), React.createElement(Legend, null), cols.map((item, index) => React.createElement(Bar, {
    dataKey: item,
    fill: d3.interpolateRdYlBu((index + 1) / cols.length)
  }))), document.querySelector('#pub-distribution-chart'));
});