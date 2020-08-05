d3.csv('/nbextensions/topic_distribution.csv', processData).then(data => {

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
  
    const CustomTooltip = ({
      active,
      payload,
      label
    }) => {
      if (active) {
        return React.createElement("div", {
          className: "custom-tooltip"
        }, React.createElement("p", null, React.createElement("span", {
          className: "label"
        }, " ", ` Topic ${label}: ${nrformat(payload[0].value)} %`, " ")));
      }
  
      return null;
  
      function nrformat(num) {
        num = +num;
        return num.toFixed(2);
      }
    };
  
    ReactDOM.render( React.createElement(BarChart, {
      width: 400,
      height: 200,
      data: data,
      margin: {
        top: 5,
        right: 30,
        left: 20,
        bottom: 10
      }
    }, React.createElement(CartesianGrid, {
      strokeDasharray: "3 3"
    }), React.createElement(XAxis, {
      dataKey: "topics"
    }, React.createElement(Label, {
      value: "Topics",
      offset: -7,
      position: "insideBottom"
    })), React.createElement(YAxis, {
      dataKey: data.topics
    }, React.createElement(Label, {
      value: "Weight (%)",
      offset: 12,
      position: "insideLeft",
      angle: -90
    })), React.createElement(Tooltip, {
      content: React.createElement(CustomTooltip, null)
    }), React.createElement(Bar, {
      dataKey: "weight",
      fill: "steelblue"
    })), document.querySelector('#topic-prop-chart'));
  });