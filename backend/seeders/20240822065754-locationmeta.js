'use strict';
let data = require("../data/moredestinations.json");

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    const cleanedData = data.map(location => ({
      id: location.id,
      title: location.title,
      link: location.link,
      cid: location.cid,
      category: location.category,
      review_rating: location.review_rating,
      latitude: location.latitude,
      longtitude: location.longtitude,
      timezone: location.timezone,
      images: JSON.stringify(location.images),
      createdAt: new Date(),
      updatedAt: new Date()
    }));

    await queryInterface.bulkInsert('MetaLocations', cleanedData);
  },

  async down(queryInterface, Sequelize) {
    await queryInterface.bulkDelete('MetaLocations', null, {});
  }
};
