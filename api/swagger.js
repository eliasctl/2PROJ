import swaggerAutogen from 'swagger-autogen';

const doc = {
    info: {
      title: 'API 2PROJ Paris 1'
    },
    host: 'localhost:3001'
  };

const outputFile = './swagger_output.json'
const endpointsFiles = ['./index.js']

swaggerAutogen(outputFile, endpointsFiles, doc)