d3.csv('/nbextensions/distribution_per_year.csv').then(data => {
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
      width: 1000,
      height: 400,
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
      dataKey: "year"
    }), React.createElement(YAxis, null), React.createElement(Tooltip, null), React.createElement(Legend, null), cols.map((item, index) => React.createElement(Bar, {
      dataKey: item,
      fill: d3.interpolateRdYlBu((index + 1) / cols.length)
    }))), document.querySelector('#pub-distribution-year-bar'));
  });