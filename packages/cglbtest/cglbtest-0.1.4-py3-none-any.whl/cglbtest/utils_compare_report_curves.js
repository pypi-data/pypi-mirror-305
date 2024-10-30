const curvemgmt = {
  // GENERIC
  curve_add_chart: function(element_parent, data) {
    // create div
    const div = document.createElement('div');
    // div.style.cssText = "width: 600px; height: 400px;";
    div.style.cssText = "width: 400px; height: 300px;";
    element_parent.appendChild(div);
    // chart
    const parameter = dom.getRadio("parameters", "js_lib")
    switch (parameter) {
      case "plotly":
        chartlibs.plotly.add(
          div,
          { title: data.title, xaxis: data.xaxis , yaxis: data.yaxis },
          data.series.map((item) => {return {
            name:   item.name,
            color:  item.color,
            x_data: item.data.map((e) => e[0]),
            y_data: item.data.map((e) => e[1]),
          }}),
        )
        break;
      case "echarts": 
        chartlibs.echarts.add(div, data);
        break;
    }
  },
  // SIMPLE
  // GROUPS
  curve_add_group: function(test_index, group_index) {

    // context
    const curves = {
      test:      global_curves.test[test_index],
      reference: global_curves.reference[test_index],
    }        
    const chart = curves.test.charts[chart_index]

    // elements mgmt
    const test_element_id = `curves_${parseInt(test_index)+1}`
    const group_element_id = `${test_element_id}_${parseInt(group_index)}`
    let group_element = dom.get(group_element_id)
    if (! group_element ) {
      group_element = document.createElement('div');
      group_element.id = group_element_id
      dom.get(test_element_id).appendChild(group_element);
    } else {
      group_element.innerHTML = "";
    }
    group_element.innerHTML = '<div style="margin:10px 0px;"><strong>' + chart.title + '</strong></div>';
    
    group_element_charts = document.createElement('div');
    group_element_charts.style.cssText = "display: flex;flex-wrap: wrap;";
    group_element.appendChild(group_element_charts);

    // display test and reference
    const curve_0 = curves.test.curves[chart.curves[0]]
    const labels = { test: "Test", reference: "Reference" }
    for (type in labels) {

      const series = []
      chart.curves.forEach(curve_index => {
        const curve = curves[type].curves[curve_index]
        series.push({
          name:  curve.short_title,
          data:  curve.series,
          color: null,
        })
      });
      
      const data = {
        title: chart.title + " [" + labels[type] + "]",
        xaxis: chart.xaxis,
        yaxis: chart.yaxis,
        series : series,
      }
      this.curve_add_chart(group_element_charts, data)
    }

    // if one curve same line else new div
    if (chart.curves.length > 1) {
      group_element_charts = document.createElement('div');
      group_element_charts.style.cssText = "display: flex;flex-wrap: wrap;";
      group_element.appendChild(group_element_charts);
    } 

    // display ecah curve test vs reference
    for (index_curve in chart.curves) {
      real_index = chart.curves[index_curve]

      const series = [
        {
          name:  "Test",
          data:  curves["test"].curves[real_index].series,
          color: '#1982c4',
        },
        {
          name:  "Reference",
          data:  curves["reference"].curves[real_index].series,
          color: '#6a4c93',
        },
      ]
      const data = {
        title: curves["test"].curves[real_index].title + " [Test vs Reference]",
        xaxis: chart.xaxis,
        yaxis: chart.yaxis,
        series : series,
      }
      this.curve_add_chart(group_element_charts, data)
    }
  },
  load_group_curves: function() {
    // call chart group
    for (i in global_curves.test) {
      if (global_curves.test[i]) {
        for (chart_index in global_curves.test[i].charts) {
          this.curve_add_group(i, chart_index)
        }
      }
    }
  },
};