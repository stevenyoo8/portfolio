printjson("****************************************************************");
printjson("1) Document insert with insertOne()");
printjson(db.data.insertOne({_id: ObjectId("653b274151312edcf71afd69"),
                             position: {type: "Point", coordinates: [10, 20]}, 
                             callLetters: "PLAT", 
                             airTemperature: {value: -5.0, quality: "1"}, 
                             pressure: {value: 1015.3, quality: "1"}, 
                             sections: ["AG1", "AY1", "GF1", "MD1", "MW1", "SA1", "UA1", "UG1"]}));

printjson("****************************************************************");
printjson("2) Document insert with insertMany()");
printjson(db.data.insertMany([
    {
     position: {type: "Point", coordinates: [10, 20]}, 
     callLetters: "PLAT", 
     airTemperature: {value: -5.0, quality: "1"}, 
     pressure: {value: 1015.3, quality: "1"}, 
     sections: ["AG1", "AY1", "GF1", "MD1", "MW1", "SA1", "UA1", "UG1"]
    },
    {
    position: {type: "Point", coordinates: [17, 2.5]},
    callLetters: "VCNP",
    airTemperature: {value: 2.5, quality: "2"},
    pressure: {value: 506.8, quality: "1"},
    sections: ["AG1", "MD1", "UG1"]
    }
]));


printjson("****************************************************************");
printjson("3) Document insert with insertMany()");
printjson(db.data.insertMany([
    {
     position: {type: "Point", coordinates: [1.5, 47.5]}, 
     callLetters: "CG26", 
     airTemperature: {value: -17.4, quality: "1"}, 
     pressure: {value: 10, quality: "1"}, 
     sections: ["MW1", "SA1", "UA1", "UG1"]
    },
    {
    position: {type: "Point", coordinates: [5.6, 1.2]},
    callLetters: "VCNP",
    airTemperature: {value: 25, quality: "1"},
    pressure: {value: 1257.3, quality: "2"},
    sections: "AG1"
    }
]));

printjson("****************************************************************");
printjson("4) Document update with updateOne()");
printjson(db.data.updateOne(
    {_id: ObjectId("653b274151312edcf71afd69")},
    {$set: {
        position: {type: "Point", coordinates: [6.5, 2.0]},
        callLetters: "UYOK",
        airTemperature: { value: -5.0, quality: "1" },
        pressure: { value: 1015.3, quality: "1" },
        sections: ["AG1", "AY1", "GF1", "MD1", "MW1", "SA1", "UA1", "UG1"]}}));

printjson("****************************************************************");
printjson("5) Document update with updateOne() and $push");
printjson(db.data.updateOne({_id: ObjectId("653b274151312edcf71afd69")}, {$push: {"position.coordinates": [6.5, 5.1], sections: ["AG1", "SA1", "UA1", "UG1"]}}));

printjson("****************************************************************");
printjson("6) Document update with updateMany()");
printjson(db.data.updateMany(
    {callLetters: "VCNP"},
    {$set: {
        position: {type: "Point", coordinates: [4.7, 8.1]},
        airTemperature: {value: 12.5, quality: "2"},
        pressure: { value: 1273.5, quality: "1" },
        sections: ["AG1",, "SA1", "UA1", "UG1"]}}));

printjson("****************************************************************");
printjson("7) Document update with updateMany()");
printjson(db.data.updateMany(
    {type: "FM-13"},
    {$set: {
        position: {type: "Point", coordinates: [6.7, 50.6]},
        callLetters: "CG26",
        airTemperature: {value: -4.7, quality: "1"},
        pressure: { value: 945.2, quality: "2" },
        sections: "MW1"}}));

printjson("****************************************************************");
printjson("8) Document delete with deleteOne()");
printjson(db.data.deleteOne({_id: ObjectId("653b274151312edcf71afd69")}));

printjson("****************************************************************");
printjson("9) Document delete with deleteMany()");
printjson(db.data.deleteMany({"airTemperature.value": {$gt: 10}, 
  callLetters: "CG26", 
  type: "FM-13", 
  "pressure.value": {$gt: 500}, 
  "visibility.distance.value": {$gt: 5000}}));

printjson("****************************************************************");
printjson("10) Document delete with deleteMany()");
printjson(db.data.deleteMany({
    "elevation": 9999, 
    callLetters: "TFWI", 
    type: "FM-13", 
    "dewPoint.value": 999.9, 
    "skyCondition.ceilingHeight.value": 99999}));