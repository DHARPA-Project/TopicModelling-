d3.csv('nbextensions/coherence_table.csv', removeSpaces).then(data => {
  data['nr_topics'] = data['Number of topics'];

  class TempTable extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        Topics: '4'
      };
      this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
      this.setState({
        Topics: event.target.value
      });
    }

    render() {
      const dataset = data;
      var entries = d3.nest().key(function (d) {
        return d.Number_of_topics;
      }).entries(dataset);
      var user_select = this.state.Topics;
      var data_filtered = dataset.filter(function (d) {
        return d.Number_of_topics === user_select;
      });
      return React.createElement("div", null, React.createElement("select", {
        className: "ui selection dropdown",
        value: this.state.Topics,
        onChange: this.handleChange
      }, entries.map(item => React.createElement("option", {
        key: item.key,
        value: item.key
      }, "Number of topics: ", item.key))), React.createElement("table", {
        className: "ui collapsing table unstackable"
      }, React.createElement("thead", null, React.createElement("tr", null, React.createElement("th", null, "Topic"), React.createElement("th", null, "Topic words"))), React.createElement("tbody", null, data_filtered.map(item => React.createElement("tr", null, React.createElement("td", {
        "data-label": "Topic"
      }, item['Topic']), React.createElement("td", {
        "data-label": "Topic words"
      }, item['Topic_words']))))));
    }

  }

  ReactDOM.render( React.createElement(TempTable, null), document.querySelector('#coherence-table'));
});

function removeSpaces(d) {
  Object.keys(d).forEach(function (origProp) {
    const noSpace = replaceAll(origProp, " ", "_");
    d[noSpace] = d[origProp];
  });
  return d;
}

;

function replaceAll(string, search, replace) {
  return string.split(search).join(replace);
}