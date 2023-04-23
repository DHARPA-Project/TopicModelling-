d3.csv('/nbextensions/rolling_mean.csv').then(data => {
    const cols1 = data.columns.slice(2);
    const cols = cols1.map(item => {
      const nr = item.match(/(\d+)/);
      const top_nr = +nr[0];
      return `Topic ${top_nr}`;
    });
    const colors = cols.map((item, index) => {
      d3.interpolateTurbo((index + 1) / cols.length);
    });
    const {
      LineChart,
      Line,
      Label,
      Cell,
      XAxis,
      YAxis,
      CartesianGrid,
      Tooltip,
      Legend
    } = Recharts;
    ReactDOM.render( React.createElement(LineChart, {
      width: 600,
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
      dataKey: "year",
      padding: {
        left: 30,
        right: 30
      }
    }), React.createElement(YAxis, null), React.createElement(Tooltip, null), React.createElement(Legend, null), cols1.map((item, index) => React.createElement(Line, {
      type: "monotone",
      dataKey: item,
      stroke: d3.interpolateRdYlBu((index + 1) / cols.length)
    }))), document.querySelector('#rolling-mean-chart'));
  });