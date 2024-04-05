// cloud-functions/index.js

const functions = require('firebase-functions');
const admin = require('firebase-admin');

admin.initializeApp();

const db = admin.firestore();

exports.monitorEndpoints = functions.pubsub.schedule('every 1 minutes').onRun(async (context) => {
  const endpointsRef = db.collection('endpoints');
  const snapshot = await endpointsRef.get();

  const updates = {};
  snapshot.forEach(doc => {
    const endpoint = doc.data();
    // Simulate endpoint status update based on logic provided
    const status = Math.random() < 0.8 ? 'Stable' : 'Unstable';
    updates[doc.id] = { status };
  });

  await endpointsRef.doc().update(updates);
});
