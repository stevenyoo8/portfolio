printjson("****************************************************************");
printjson("1) Locations with temperature between 10 and 20 degrees Celcius");
printjson(db.data.find({'airTemperature.value': {$gt: 10, $lt: 20}}, {position: 1, airTemperature: 1, pressure: 1, wind: 1, _id: 0}).sort({"airTemperature.value": 1}).limit(5));

printjson("****************************************************************");
printjson("2) Location with section UG1");
printjson(db.data.find({sections: "UG1"}, {position: 1, callLetters: 1, type: 1, sections: 1, _id: 0}).limit(5));

printjson("****************************************************************");
printjson("3) Location with visibility less than 20000 and wind direction angle less than 100");
printjson(db.data.find({$and: [{"visibility.distance.value": {$lt: 20000}}, {"wind.direction.angle": {$lt: 100}}]}, {position: 1, airTemperature: 1, visibility: 1, wind: 1, _id: 0}).sort({"visibility.distance.value": 1}).limit(5));

printjson("****************************************************************");
printjson("4) Location with type FM-13 and quaility control process V020");
printjson(db.data.find({$and: [{type: "FM-13"}, {qualityControlProcess: "V020"}]}, {position: 1, st: 1, ts: 1, callLetters: 1, qualityControlProcess: 1, type: 1, _id: 0}).sort({ts: 1}).limit(5));

printjson("****************************************************************");
printjson("5) Location with a presentWeatherObservationManual element with a condition of 04");
printjson(db.data.find({presentWeatherObservationManual: {$elemMatch: {condition: "04"}}}, {position: 1, ts: 1, pastWeatherObservationManual: 1, presentWeatherObservationManual: 1, _id: 0}).sort({ts: 1}).limit(5));

printjson("****************************************************************");
printjson("6) Location with section GF1 or MW1");
printjson(db.data.find({$or: [{sections: "GF1"}, {sections: "MW1"}]}, {position: 1, callLetters: 1, type: 1, sections: 1, _id: 0}).limit(5));

printjson("****************************************************************");
printjson("7) Location with waves that have a height of 1 or a wind speed between 10 and 12 that have a wave measurement");
printjson(db.data.find({$or: [{"waveMeasurement.waves.height": 1},  {"wind.speed.rate": {$lt: 12, $gt: 10}}], "waveMeasurement.waves.height": {$gte: 0}}, {position: 1, ts: 1, wind: 1, waveMeasurement: 1, _id: 0}).sort({"waveMeasurement.waves.period": 1}).limit(5));

printjson("****************************************************************");
printjson("8)Location with coordinates having latitude equal to -2.1, sorted by longitude");
printjson(db.data.find({"position.coordinates.0": -2.1}, {position: 1, type: 1}).sort({"position.coordinates.1": 1}).limit(5));

printjson("****************************************************************");
printjson("9) Locations where visibility distance is between 1 and 999, and wind speed is greater than 10");
printjson(db.data.find({"visibility.distance.value": {$gte: 1, $lte: 999}, "wind.speed.rate": {$gt: 10}}, {position: 1, visibility: 1, wind: 1}).sort({"wind.speed.rate": 1}).limit(5));

printjson("****************************************************************");
printjson("10) Locations where sections contain AG1, MD1, OA1, UA1, and SA1, and call letters are PLAT, sorted by their air temperature.");
printjson(db.data.find({sections: {$all: ["AG1", "MD1", "OA1", "SA1", "UA1"]}, callLetters: "PLAT"}, {position: 1, callLetters: 1, sections: 1, airTemperature: 1}).sort({airTemperature: 1}).limit(5));