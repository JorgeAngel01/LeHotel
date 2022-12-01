var series = {
  monthDataSeries1: {
    prices: [],
    dates: [],
  },
};

// Grafico M-Ing Reservaciones
var options = {
  series: [
    {
      name: "STOCK ABC",
      data: series.monthDataSeries1.prices,
    },
  ],
  chart: {
    type: "area",
    height: 350,
    zoom: {
      enabled: true,
    },
  },
  dataLabels: {
    enabled: false,
  },
  stroke: {
    curve: "straight",
  },
  labels: series.monthDataSeries1.dates,
  xaxis: {
    type: "datetime",
  },
  yaxis: {
    opposite: true,
  },
  legend: {
    horizontalAlign: "left",
  },
  subtitle: {
    text: '',
    align: 'left'
  },
};

const value = JSON.parse(
  JSON.parse(document.getElementById("data_mes").textContent)
);
console.log(value);

var costo_acum = 0;
var fecha_ant = new Date();
var total = 0;

if (value.length > 1) {
  for (var i = 0; i < value.length; i++) {
    var objs = value[i];

    precio = parseFloat(objs.fields.costo_reservado);
    fecha = new Date(objs.fields.fecha_reserva + " 00:00:00");

    if (fecha_ant != fecha && i != 0) {
      series.monthDataSeries1.dates.push(fecha_ant.toString());
      series.monthDataSeries1.prices.push(costo_acum);
      total += costo_acum;
      costo_acum = 0;
    }

    costo_acum += parseFloat(precio);
    fecha_ant = fecha;
  }
  series.monthDataSeries1.dates.push(fecha_ant.toString());
  series.monthDataSeries1.prices.push(costo_acum);
  total += costo_acum;
} else {
  if (value.length != 0) {
    var objs = value[0];
    precio = objs.fields.costo_reservado;
    fecha = new Date(objs.fields.fecha_reserva + " 00:00:00");
    series.monthDataSeries1.dates.push(fecha.toString());
    series.monthDataSeries1.prices.push(precio);
    total += precio;
  }
}

options.subtitle.text = "Total: $" + total.toString()

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();

// Grafico S-Ing Reservaciones
var series = {
  monthDataSeries1: {
    prices: [],
    dates: [],
  },
};

var options = {
  series: [
    {
      name: "STOCK ABC",
      data: series.monthDataSeries1.prices,
    },
  ],
  chart: {
    type: "area",
    height: 350,
    zoom: {
      enabled: true,
    },
  },
  dataLabels: {
    enabled: false,
  },
  stroke: {
    curve: "straight",
  },
  labels: series.monthDataSeries1.dates,
  xaxis: {
    type: "datetime",
  },
  yaxis: {
    opposite: true,
  },
  legend: {
    horizontalAlign: "left",
  },
  subtitle: {
    text: '',
    align: 'left'
  },
};

const val = JSON.parse(
  JSON.parse(document.getElementById("data_sem").textContent)
);
console.log(val);

costo_acum = 0;
fecha_ant = new Date();
total = 0

if (val.length > 1) {
  for (var i = 0; i < val.length; i++) {
    var objs = val[i];

    precio = parseFloat(objs.fields.costo_reservado);
    fecha = new Date(objs.fields.fecha_reserva + " 00:00:00");

    if (fecha_ant != fecha && i != 0) {
      series.monthDataSeries1.dates.push(fecha_ant.toString());
      series.monthDataSeries1.prices.push(costo_acum);
      total += costo_acum;
      costo_acum = 0;
    }

    costo_acum += parseFloat(precio);
    fecha_ant = fecha;
  }
  series.monthDataSeries1.dates.push(fecha_ant.toString());
  series.monthDataSeries1.prices.push(costo_acum);
  total += costo_acum;
} else {
  if (val.length != 0) {
    var objs = val[0];

    precio = objs.fields.costo_reservado;
    fecha = new Date(objs.fields.fecha_reserva + " 00:00:00");
    series.monthDataSeries1.dates.push(fecha.toString());
    series.monthDataSeries1.prices.push(precio);
    total += precio;
  }
}

options.subtitle.text = "Total: $" + total.toString()

var chart2 = new ApexCharts(document.querySelector("#chart2"), options);
chart2.render();

function clickM() {
  $("#label-ing").text("Ultimo Mes: ");
  document.getElementById("week-ing").style.display = "None";
  document.getElementById("month-ing").style.display = "block";
}
function clickS() {
  $("#label-ing").text("Ultima Semana:");
  document.getElementById("month-ing").style.display = "None";
  document.getElementById("week-ing").style.display = "block";
}

/*var series = 
{
  "monthDataSeries1": {s
    "prices": [
      8107.85,
      8128.0,
      8122.9,
      8165.5,
      8340.7,
      8423.7,
      8423.5,
      8514.3,
      8481.85,
      8487.7,
      8506.9,
      8626.2,
      8668.95,
      8602.3,
      8607.55,
      8512.9,
      8496.25,
      8600.65,
      8881.1,
      9340.85
    ],
    "dates": [
      "13 Nov 2017",
      "14 Nov 2017",
      "15 Nov 2017",
      "16 Nov 2017",
      "17 Nov 2017",
      "20 Nov 2017",
      "21 Nov 2017",
      "22 Nov 2017",
      "23 Nov 2017",
      "24 Nov 2017",
      "27 Nov 2017",
      "28 Nov 2017",
      "29 Nov 2017",
      "30 Nov 2017",
      "01 Dec 2017",
      "04 Dec 2017",
      "05 Dec 2017",
      "06 Dec 2017",
      "07 Dec 2017",
      "08 Dec 2017"
    ]
  }
}*/
