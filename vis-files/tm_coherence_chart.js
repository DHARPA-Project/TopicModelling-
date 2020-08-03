d3.csv('/nbextensions/coherence_values.csv').then(data => {
    const {
      LineChart,
      Line,
      Label,
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
        }, " ", `${payload[0].name}: `, "  "), React.createElement("span", {
          className: "desc"
        }, " ", `${nrformat(payload[0].value)}`, " ")), React.createElement("p", null, React.createElement("span", {
          className: "label"
        }, " ", `Number of topics: `, "  "), React.createElement("span", {
          className: "desc"
        }, " ", `${label}`, " ")));
      }

      return null;
    };

    function nrformat(num) {
      num = +num;
      return num.toFixed(3);
    }

    ReactDOM.render( React.createElement(LineChart, {
      width: 500,
      height: 300,
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
      dataKey: "Number of topics",
      padding: {
        left: 20,
        right: 20
      }
    }, React.createElement(Label, {
      value: "Number of topics",
      offset: -7,
      position: "insideBottom"
    })), React.createElement(YAxis, {
      dataKey: "Coherence",
      padding: {
        top: 20,
        bottom: 20
      }
    }, React.createElement(Label, {
      value: "Coherence",
      offset: -7,
      position: "insideLeft",
      angle: -90
    })), React.createElement(Tooltip, {
      content: React.createElement(CustomTooltip, null),
      animationDuration: 20
    }, " "), React.createElement(Line, {
      type: "monotone",
      dataKey: "Coherence",
      stroke: "#4682b4",
      activeDot: {
        r: 8
      }
    })), document.querySelector('#coherence-chart'));
    });