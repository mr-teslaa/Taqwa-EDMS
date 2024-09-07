(function() {
    const Option = {
        series: [{
                name: 'series1',
                data: [4.6, 3.6, 2, 3, 4, 2.4, 2.8, 4.3, 2, 1.6],
            },
            {
                name: 'series2',
                data: [1.5, 2, 3.8, 3.5, 2.2, 3.5, 4, 3, 1.5, 3.8],
            },
        ],
        chart: {
            height: 230,
            type: 'area',
            offsetY: 12,
            offsetX: -15,
            toolbar: {
                show: false,
            },
        },
        dataLabels: {
            enabled: false,
        },
        colors: [MofiAdminConfig.primary, MofiAdminConfig.secondary],

        stroke: {
            curve: 'smooth',
            width: 2,
        },
        grid: {
            show: true,
            strokeDashArray: 5,
            position: 'back',
            xaxis: {
                lines: {
                    show: false
                }
            },
        },
        fill: {
            type: 'gradient',
            gradient: {
                shadeIntensity: 1,
                inverseColors: false,
                opacityFrom: 0.45,
                opacityTo: 0.05,
                stops: [5, 100, 100, 100]
            },
        },
        annotations: {
            xaxis: [{
                x: 312,
                strokeDashArray: 5,
                borderWidth: 3,
                borderColor: MofiAdminConfig.primary,
            }, ],
            points: [{
                x: 312,
                y: 4.5,
                marker: {
                    size: 8,
                    fillColor: MofiAdminConfig.primary,
                    strokeColor: "#ffffff",
                    strokeWidth: 4,
                    radius: 5,
                },
                label: {
                    borderWidth: 1,
                    offsetY: 0,
                    text: '7h a week on average in Apr',
                    style: {
                        fontSize: '14px',
                        fontWeight: '600',
                        fontFamily: 'Outfit, sans-serif',
                    }
                }
            }],
        },
        yaxis: {
            labels: {
                show: true,
                style: {
                    fontFamily: 'Outfit, sans-serif',
                    fontWeight: 500,
                    colors: '#3D434A',
                },

                formatter: (value) => {
                    return `${value}h`;
                },
            },
        },
        xaxis: {
            type: 'category',
            categories: [
                'Jan',
                'Feb',
                'Mar',
                'Apr',
                'May',
                'Jun',
                'Jul',
                'Aug',
                'Sep',
                'Oct',
            ],
            tickAmount: 12,
            labels: {
                minHeight: undefined,
                maxHeight: 28,
                offsetX: 10,
                offsetY: 0,
                style: {
                    fontFamily: 'Outfit, sans-serif',
                    fontWeight: 500,
                    colors: '#8D8D8D',
                },
                tooltip: {
                    enabled: false,
                },
            },
            axisBorder: {
                show: false
            },
        },
        tooltip: {
            custom: function({
                series,
                seriesIndex,
                dataPointIndex,
                w
            }) {
                return `<div class="apex-tooltip"> 
                      <span>
                           <span class="bg-secondary"> </span>
                            Selling : ${series[0][dataPointIndex]} K
                      </span> 
                      <span class="mt-2">
                           <span class="bg-primary"> </span>
                            Selling : ${series[1][dataPointIndex]} K
                      </span> 
                    </div>`;
            },
        },
        legend: {
            show: false,
        },
        responsive: [{
            breakpoint: 1657,
            options: {
                chart: {
                    height: 190,
                },
            },
        }, ],
    };

    const ChartEl = new ApexCharts(document.querySelector('#study-statistics'), Option);
    ChartEl.render();

    var options = {
        series: [{
            name: 'PRODUCT A',
            data: [2, 4, 3.8, 3, 4, 3, 2]
        }, {
            name: 'PRODUCT B',
            data: [5, 4, 5, 5, 4, 5, 5]
        }, {
            name: 'PRODUCT C',
            data: [7, 6, 6, 7, 6, 4, 7]
        }, {
            name: 'PRODUCT C',
            data: [8.9, 8.9, 8.9, 8.9, 8.9, 8.9, 8.9]
        }, ],
        chart: {
            type: 'bar',
            height: 345,
            stacked: true,
            toolbar: {
                show: false
            },
            zoom: {
                enabled: false
            }
        },
        stroke: {
            show: true,
            width: [4, 4, 4, 4],
            colors: ['#ffffff', '#ffffff', '#ffffff', '#ffffff']
        },
        responsive: [{
                breakpoint: 480,
                options: {

                    legend: {
                        show: false,
                    }
                }

            },
            {
                breakpoint: 1200,
                options: {
                    chart: {
                        height: 200,
                    },
                    series: [{
                        name: 'PRODUCT A',
                        data: [2, 4, 3.8, 3, 4, 3, 2]
                    }, {
                        name: 'PRODUCT B',
                        data: [5, 4, 5, 5, 4, 5, 5]
                    }, {
                        name: 'PRODUCT C',
                        data: [7, 6, 6, 7, 6, 4, 7]
                    }, {
                        name: 'PRODUCT C',
                        data: [1, 2, 2, 1, 2, 2, 1]
                    }, ],
                }

            },
            {
                breakpoint: 768,
                options: {
                    chart: {
                        height: 345,
                    },
                    series: [{
                        name: 'PRODUCT A',
                        data: [2, 4, 3.8, 3, 4, 3, 2]
                    }, {
                        name: 'PRODUCT B',
                        data: [5, 4, 5, 5, 4, 5, 5]
                    }, {
                        name: 'PRODUCT C',
                        data: [7, 6, 6, 7, 6, 4, 7]
                    }, {
                        name: 'PRODUCT C',
                        data: [8.9, 8.9, 8.9, 8.9, 8.9, 8.9, 8.9]
                    }, ],
                }

            },
            {
                breakpoint: 436,
                options: {
                    chart: {
                        height: 345,
                    },
                    series: [{
                        name: 'PRODUCT A',
                        data: [2, 4, 3.8, 3, 4]
                    }, {
                        name: 'PRODUCT B',
                        data: [5, 4, 5, 5, 4]
                    }, {
                        name: 'PRODUCT C',
                        data: [7, 6, 6, 7, 6]
                    }, {
                        name: 'PRODUCT C',
                        data: [8.9, 8.9, 8.9, 8.9, 8.9]
                    }, ],
                }

            },
        ],

        colors: ['#C95E9E', '#D77748', MofiAdminConfig.secondary, MofiAdminConfig.primary],
        plotOptions: {
            bar: {
                horizontal: false,
                borderRadius: 2,
                columnWidth: '38%',
                dataLabels: {
                    total: {
                        show: false,
                    }
                }
            },
        },
        grid: {
            show: true,
            strokeDashArray: 5,
            position: 'back',
            xaxis: {
                lines: {
                    show: false
                }
            },
        },
        xaxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Feb', 'Feb'],
            labels: {
                show: true,
                style: {
                    fontFamily: 'Outfit, sans-serif',
                    fontWeight: 500,
                    colors: '#8D8D8D',
                },
            },
            axisBorder: {
                show: false
            },
            axisTicks: {
                show: false
            },
        },
        legend: {
            show: false,
        },
        dataLabels: {
            enabled: false,
        },
        fill: {
            opacity: 1
        },
        yaxis: {
            labels: {
                style: {
                    fontFamily: 'Outfit, sans-serif',
                    fontWeight: 500,
                    colors: '#3D434A',
                },
            },
        }
    };

    var chart = new ApexCharts(document.querySelector("#actively-hours"), options);
    chart.render();

    var options = {
        series: [{
            name: 'Website Blog',
            type: 'column',
            data: [20, 38, 18, 30, 50, 32, 60, 39, 79, 50, 40, 50, 40, 24, 65, 42]
        }, {
            name: 'Social Media',
            type: 'line',
            data: [10, 22, 36, 49, 62, 78, 90, 98, 97, 90, 78, 62, 49, 36, 22, 10]
        }],
        chart: {
            height: 315,
            type: 'line',
            offsetX: -15,
            toolbar: {
                show: false
            },
        },
        stroke: {
            width: [0, 3]
        },
        grid: {
            show: true,
            borderColor: 'rgba(106, 113, 133, 0.30)',
            strokeDashArray: 3,
        },
        dataLabels: {
            enabled: false,
        },
        fill: {
            type: 'gradient',
            opacity: 1,
            gradient: {
                shade: 'light',
                type: "vertical",
                opacityFrom: 1,
                opacityTo: 0,
                stops: [0, 80, 100],
            },
        },
        markers: {
            discrete: [{
                seriesIndex: 1,
                dataPointIndex: 0,
                fillColor: MofiAdminConfig.primary,
                strokeColor: '#fff',
                size: 5,
                shape: "circle"
            }, {
                seriesIndex: 1,
                dataPointIndex: 7,
                fillColor: MofiAdminConfig.primary,
                strokeColor: '#fff',
                size: 5,
                shape: "circle"
            }, {
                seriesIndex: 1,
                dataPointIndex: 12,
                fillColor: MofiAdminConfig.primary,
                strokeColor: '#fff',
                size: 5,
                shape: "circle"
            }, {
                seriesIndex: 1,
                dataPointIndex: 15,
                fillColor: MofiAdminConfig.primary,
                strokeColor: '#fff',
                size: 5,
                shape: "circle"
            }, ],
        },
        plotOptions: {
            bar: {
                horizontal: false,
                borderRadius: 4,
                columnWidth: '60%',
            },
        },
        colors: [MofiAdminConfig.primary, MofiAdminConfig.secondary],
        legend: {
            show: false,
        },
        labels: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        xaxis: {
            categories: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '08', '09', '10', '11'],
            labels: {
                show: true,
                style: {
                    fontFamily: 'Outfit, sans-serif',
                    fontWeight: 500,
                    colors: '#8D8D8D',
                },
            },
            axisBorder: {
                show: false
            },
        },
        yaxis: {
            labels: {
                show: true,
                style: {
                    fontFamily: 'Outfit, sans-serif',
                    fontWeight: 500,
                    colors: '#3D434A',
                },

                formatter: (value) => {
                    return `${value}%`;
                },
            },
        },
    };

    var chart = new ApexCharts(document.querySelector("#monthly-reportchart"), options);
    chart.render();

    // schedule chart
    var scheduleoptions = {
        series: [{
            data: [{
                    x: "Branding",
                    y: [
                        new Date("2024-01-01").getTime(),
                        new Date("2024-01-30").getTime(),
                    ],
                    fillColor: "var(--theme-default)",
                },
                {
                    x: "Web Design",
                    y: [
                        new Date("2024-02-20").getTime(),
                        new Date("2024-03-20").getTime(),
                    ],
                    fillColor: "#48A3D7",
                },
                {
                    x: "UX research",
                    y: [
                        new Date("2024-01-25").getTime(),
                        new Date("2024-02-25").getTime(),
                    ],
                    fillColor: "#D77748",
                },
                {
                    x: "Mobile Design",
                    y: [
                        new Date("2024-01-01").getTime(),
                        new Date("2024-02-01").getTime(),
                    ],
                    fillColor: "#C95E9E",
                },
                {
                    x: "NFT Website",
                    y: [
                        new Date("2024-02-20").getTime(),
                        new Date("2024-03-20").getTime(),
                    ],
                    fillColor: "#0DA759",
                },
                {
                    x: "Logo Design",
                    y: [
                        new Date("2024-01-25").getTime(),
                        new Date("2024-02-25").getTime(),
                    ],
                    fillColor: "var(--theme-default)",
                },
            ],
        }, ],
        chart: {
            height: 355,
            type: "rangeBar",
            toolbar: {
                show: false,
            },
        },
        plotOptions: {
            bar: {
                horizontal: true,
                distributed: true,
                barHeight: "40%",
                dataLabels: {
                    hideOverflowingLabels: false,
                },
            },
        },
        dataLabels: {
            enabled: true,
            formatter: function(val, opts) {
                var label = opts.w.globals.labels[opts.dataPointIndex];
                return label;
            },
            textAnchor: "middle",
            offsetX: 0,
            offsetY: 0,
            style: {
                fontSize: '16px',
                fontFamily: 'Outfit, sans-serif',
            },
            background: {
                enabled: true,
                padding: 6,
                borderRadius: 12,
                borderWidth: 0,
                borderColor: "var(--white)",
                opacity: 0,
            },
        },
        xaxis: {
            type: "datetime",
            position: "top",
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
            labels: {
                style: {
                    fontFamily: 'Outfit, sans-serif',
                    fontWeight: 500,
                    colors: '#8D8D8D',
                },
            },
        },
        yaxis: {
            labels: {
                style: {
                    fontFamily: 'Outfit, sans-serif',
                    fontWeight: 500,
                    colors: '#3D434A',
                },
            },

            tooltip: {
                enabled: false,
            },
        },
        grid: {
            show: false,
            row: {
                colors: ["#F4F7F9", "#fff"],
                opacity: 1,
            },
        },
        responsive: [{
            breakpoint: 576,
            options: {
                yaxis: {
                    labels: {
                        show: false,
                    },
                },
                grid: {
                    padding: {
                        left: -10,
                    },
                },
            },
        }, ],
    };

    var schedulechart = new ApexCharts(
        document.querySelector("#schedulechart"),
        scheduleoptions
    );
    schedulechart.render();

    $(".featured-table table").on("click", ".remove", function(event) {
        var ndx = $(this).parent().index() + 1;
        $("tr", event.delegateTarget).remove(":nth-child(" + ndx + ")");
    });
})();