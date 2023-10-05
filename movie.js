const mongoose = require('mongoose');

const movieSchema = new mongoose.Schema({
  releaseDate:
  {
    type: Date,
    required:true
  },
  title: {
    type:String,
    required : true
  },
  description:
  {
    type : String,
    required : true
   },
  language:
  {
    type : String,
    required :  true
  },
  genre:
  {
    type: String,
    required : true
  },
  posters:
  {
    type: String,
    required: true
  },
  duration:
  {
    type : Number,
    required : false
  },
  director:
  {
    type: String,
    required : false
  },
  cast:
  {
    type:String,
    required: false
  },
  rating:
  {
    type : Number,
    required: false
  },
  reviews:
  {
    type : [String],
    required: false
  }
  // Add other fields as needed
});

const Movie = mongoose.model('Movie', movieSchema);

module.exports = Movie;
