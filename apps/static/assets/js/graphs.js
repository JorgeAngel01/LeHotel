
var options = {
    series: [
        {
            name: "Ocupada",
            data: [
                
            ]
        },
        
    ],
    chart: {
        height: 460,
        type: "rangeBar",
    },
    plotOptions: {
        bar: {
            horizontal: true,
            barHeight: "80%",
        },
    },
    xaxis: {
        type: "datetime",
    },
    stroke: {
        width: 1,
    },
    colors:['#F44336'],
    fill: {
        type: "solid",
        opacity: 0.6,
    },
    grid: {
        
        column: {
          colors: ['#F44336', '#E91E63', '#9C27B0']
        }
    },
    legend: {
        position: "top",
        horizontalAlign: "left",
    },
};

function Data(x, y) {
    this.x = x;
    this.y = y;
}

const value = JSON.parse(JSON.parse(document.getElementById('data').textContent));
console.log(value)

for (var i = 0; i < value.length; i++) {
    var objs = value[i]
    x = objs.fields.habitaciones.toString()  
    y = []
    a = new Date(objs.fields.fecha_reserva + ' 00:00:00').getTime() 
    b = new Date(objs.fields.fecha_entrega + ' 00:00:00').getTime() 
    /*
    a = new Date("2019-03-07").getTime() 
    b = new Date("2019-03-10").getTime()  */
    y.push(a)
    y.push(b)

    const obj = new Data(x,y);

    options.series[0].data.push(obj)

}

x = "The Green Suit"  
y = []
/*
a = new Date("2022-11-07").getTime() 
b = new Date("2022-11-10").getTime()  
y.push(a)
y.push(b)*/

const obj = new Data(x,y);

const data = []
data.push(obj)
data.push(obj)
console.log(data)

console.log(options)

console.log(options.series[0].data)

options.series[0].data.push(obj)

console.log(options.series[0].data)

var chart = new ApexCharts(document.querySelector("#chart"), options);

/*
chart.appendData(
    [{
        data: [
            {
                x: "The Green Suit", 
                y: [
                    new Date("2019-03-07").getTime(),
                    new Date("2019-03-10").getTime(),
                ]
            }
        ]
    }]
);
*/

chart.render();
