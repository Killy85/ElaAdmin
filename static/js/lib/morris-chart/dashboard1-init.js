// Dashboard 1 Morris-chart
$( function () {
	"use strict";


	// Extra chart
	Morris.Area( {
		element: 'extra-area-chart',
		data: [ {
				period: '2018-03-20',
				site1: 10,
				site2: 25,
				site3: 17,
				site4: 31
        }, {
				period: '2018-03-21',
				site1: 55,
				site2: 5,
				site3: 21,
				site4: 4
        }, {
				period: '2018-03-22',
				site1: 20,
				site2: 65,
				site3: 17,
				site4: 31
        }, {
				period: '2018-03-23',
				site1: 18,
				site2: 9,
				site3: 23,
				site4: 8
        }, {
				period: '2018-03-23',
				site1: 4,
				site2: 17,
				site3: 31,
				site4: 57
        }
        ],
		lineColors: [ '#26DAD2', '#fc6180', '#62d1f3', '#ffb64d', '#4680ff' ],
		xkey: 'period',
		ykeys: [ 'site1', 'site2', 'site3', 'site4'],
		labels: [ 'site1', 'site2', 'site3', 'site4'],
		pointSize: 0,
		lineWidth: 0,
		resize: true,
		fillOpacity: 0.8,
		behaveLikeLine: true,
		gridLineColor: '#e0e0e0',
		hideHover: 'auto'

	} );



} );
