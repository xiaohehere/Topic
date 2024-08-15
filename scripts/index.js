var symptomName = last_month_day();
var mapChart; // 全局变量，存储地图实例

// 全局变量和初始化
$(function () {
  init();
  initMapChart();

  var date = new Date();
  var today = getFormatMonth(new Date());
  $("#date1").html(today);
  $("#date2").html(today);
  $("#date3").html(today);
  $("#date4").html(today);

  lay(".demo-input").each(function () {
    laydate.render({
      type: "month",
      elem: this,
      trigger: "click",
      theme: "#95d7fb",
      calendar: true,
      showBottom: true,
      done: function () {
        console.log($("#startDate").val());
      },
    });
  });

  // 绑定文件输入的change事件
  document.getElementById('fileInput').addEventListener('change', handleFileRead);
});

// 新增函数：初始化地图
function initMapChart() {
  mapChart = echarts.init(document.getElementById("mapChart"));

  var option = {
    bmap: {
      center: [110.57266, 21.83898], // 地图中心点
      zoom: 15, // 缩放级别
      roam: true, // 是否允许漫游
    },
    series: [
      {
        name: '点位',
        type: 'scatter', // 图表类型为散点图
        coordinateSystem: 'bmap', // 坐标系为百度地图
        symbolSize: 10, // 散点图符号大小
        data: [], // 初始为空
        tooltip: { // 鼠标悬浮提示
          trigger: 'item',
          formatter: function(params) {
            return params.value[2]; // 显示名称
          }
        }
      }
    ],
    tooltip: {
      trigger: "item",
      formatter: function (params, ticket, callback) {
        return params.value[2] + ":<br>" + params.value[3];
      },
    }
  };

  mapChart.setOption(option);

  var bmap = mapChart.getModel().getComponent("bmap").getBMap();
  bmap.addControl(new BMap.MapTypeControl({
    mapTypes: [BMAP_NORMAL_MAP, BMAP_SATELLITE_MAP]
  }));
  bmap.setMapStyle({ style: "midnight" });
}

// 新增函数：处理文件读取
function handleFileRead(e) {
  var reader = new FileReader();
  reader.onload = function(e) {
    var data = e.target.result;
    console.log("File read successfully");
    parseExcelData(data);
  };
  reader.readAsArrayBuffer(e.target.files[0]);
}

// 新增函数：解析Excel数据
function parseExcelData(data) {
  var workbook = XLSX.read(data, { type: 'array' });
  console.log("Excel data parsed successfully");
  var sheetName = workbook.SheetNames[0];
  var worksheet = workbook.Sheets[sheetName];
  var excelData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
  console.log("Parsed Excel Data:", excelData);
  updateMapChart(excelData);
}

// 新增函数：更新地图图表
function updateMapChart(excelData) {
  console.log("Updating map chart with data:", excelData);

  if (!mapChart) {
    mapChart = echarts.init(document.getElementById("mapChart"));
  }

  var scatterData = excelData.map(function(row, index) {
    var longitude = parseFloat(row[5]);
    var latitude = parseFloat(row[6]);
    var name = row[2] || '';
    return {
      name: index,
      value: [longitude, latitude, name],
    };
  });

  var option = mapChart.getOption();
  option.series[0].data = scatterData;
  mapChart.setOption(option);
}

// 更新文件名显示
function updateFileName() {
    var input = document.getElementById('fileInput');
    var fileNameSpan = document.getElementById('fileName');

    // 检查用户是否选择了文件
    if (input.files.length > 0) {
        var fileName = input.files[0].name; // 获取文件名
        fileNameSpan.textContent = fileName; // 更新页面上的文件名显示
    } else {
        fileNameSpan.textContent = '没有选择文件'; // 如果没有选择文件，则显示默认提示
    }
}

// 初始化图表
function init() {
  var pieChart1 = echarts.init(document.getElementById("pieChart1"));
  pieChart1.setOption({
    color: ["#87cefa", "#ff7f50", "#32cd32", "#da70d6", "#4682b4"],
    legend: {
      y: "260",
      x: "center",
      textStyle: {
        color: "#ffffff",
      },
      data: ["茂南区", "电白区", "高州市", "化州市", "信宜市"],
    },
    tooltip: {
      trigger: "item",
      formatter: "{a}<br/>{b}<br/>{c}G ({d}%)",
    },
    calculable: false,
    series: [
      {
        name: "各区流量统计",
        type: "pie",
        radius: ["40%", "70%"],
        center: ["50%", "45%"],
        itemStyle: {
          normal: {
            label: {
              show: false,
            },
            labelLine: {
              show: false,
            },
          },
          emphasis: {
            label: {
              show: true,
              position: "center",
              textStyle: {
                fontSize: "20",
                fontWeight: "bold",
              },
            },
          },
        },
        data: [
          { value: 260554.2843, name: "茂南区" },
          { value: 204017.8907, name: "电白区" },
          { value: 174520.3932, name: "高州市" },
          { value: 144770.9772, name: "化州市" },
          { value: 124997.639, name: "信宜市" },
        ],
      },
    ],
  });

  var histogramChart = echarts.init(document.getElementById("histogramChart"));
  histogramChart.setOption({
    color: ["#87cefa", "#ff7f50", "#32cd32", "#da70d6", "#4682b4"],
    legend: {
      y: "260",
      x: "center",
      data: ["茂南区", "电白区", "高州市", "化州市", "信宜市"],
      textStyle: {
        color: "#ffffff",
      },
    },
    tooltip: {
      trigger: "item",
      formatter: "{a}<br/>{b}<br/>{c}G ({d}%)",
    },
    calculable: false,
    series: [
      {
        name: "各区话务量统计",
        type: "pie",
        radius: ["40%", "70%"],
        center: ["50%", "45%"],
        itemStyle: {
          normal: {
            label: {
              show: false,
            },
            labelLine: {
              show: false,
            },
          },
          emphasis: {
            label: {
              show: true,
              position: "center",
              textStyle: {
                fontSize: "20",
                fontWeight: "bold",
              },
            },
          },
        },
        data: [
          { value: 24531.71625, name: "茂南区" },
          { value: 21197.53437, name: "电白区" },
          { value: 18010.64255, name: "高州市" },
          { value: 17875.51276, name: "化州市" },
          { value: 12546.35518, name: "信宜市" },
        ],
      },
    ],
  });
}

// 获取图例和数据值的函数
function get_legend(data) {
  var listLegend = new Array();

  for (i = 0; i < data.length; i++) {
    n = data[i]["name"];
    listLegend.push(n);
  }
  console.log("get_legend", listLegend);
  return listLegend;
}

function get_value(data) {
  var listLegend = new Array();
  var listValue = new Array();
  for (i = 0; i < data.length; i++) {
    n = data[i][2];
    v = data[i][3];
    tmp = { name: n, value: v };
    listLegend.push(n);
    listValue.push(tmp);
  }
  console.log("get_value");
  return [listLegend, listValue];
}

function get_value2(data) {
  var listLegend = new Array();
  var listValue = new Array();
  for (i = 0; i < data.length; i++) {
    n = data[i][2];
    v = [data[i][3], data[i][4], data[i][5]];
    tmp = { name: n, data: v };
    listLegend.push(n);
    listValue.push(tmp);
  }
  console.log("get_value2");
  return [listLegend, listValue];
}

function get_value3(data) {
  var listLegend = new Array();
  var listValue = new Array();
  for (i = 0; i < data.length; i++) {
    n = data[i][2];
    v = [
      data[i][3],
      data[i][4],
      data[i][5],
      data[i][3],
      data[i][4],
      data[i][5],
      data[i][3],
      data[i][4],
      data[i][5],
    ];
    tmp = { name: n, data: v };
    listLegend.push(n);
    listValue.push(tmp);
  }
  console.log("get_value3");
  return [listLegend, listValue];
}

// 异步加载数据
function async_map_data() {
  $.getJSON("/json/map.json").done(function (data) {
    console.log("/json/map.json");
    var chartMapElement = document.getElementById("mapChart");
    var myChart = echarts.init(chartMapElement);
    console.log(data);
    myChart.setOption({
      series: [
        {
          data: data,
        },
      ],
    });

    var pieChart1Element = document.getElementById("pieChart1");
    var pieChart1 = echarts.init(pieChart1Element);
    rs = get_value(data);
    pieChart1.setOption({
      legend: {
        data: rs[0],
      },
      series: [
        {
          data: rs[1],
        },
      ],
    });

    var histogramChartElement = document.getElementById("histogramChart");
    var histogramChart = echarts.init(histogramChartElement);
    rs = get_value2(data);
    histogramChart.setOption({
      legend: {
        data: rs[0],
      },
      series: rs[1],
    });

    var lineChart = echarts.init(document.getElementById("lineChart"));
    rs = get_value3(data);
    lineChart.setOption({
      legend: {
        data: rs[0],
      },
      series: rs[1],
    });
  }); //end $.getJSON
}

// 异步加载其他数据
function async_chart_2_data() {
  $.getJSON("/json/chart_2.json").done(function (data) {
    t0 = document.getElementById("t0");
    t0.innerText = data[0];

    t1 = document.getElementById("t1");
    t1.innerText = data[1];

    t2 = document.getElementById("t2");
    t2.innerText = data[2];

    t3 = document.getElementById("t3");
    t3.innerText = data[3];

    t4 = document.getElementById("t4");
    t4.innerText = data[4];

    t5 = document.getElementById("t5");
    t5.innerText = data[5];
  }); //end $.getJSON chart_2
}
