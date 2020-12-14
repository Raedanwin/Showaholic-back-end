const express = require('express')
const methodOverride = require('method-override')
const session = require('express-session')
const axios = require('axios')

require('dotenv').config()
const app = express()
// const db = 
const PORT = 3001

// MIDDLEWARE
app.use(methodOverride('_method'))
app.use(express.urlencoded({ extended: true }))
app.use(express.static('public'))

// DATABASE

// CONTROLLERS

// ROUTES
app.get('/', (req, res) => {
    res.redirect('/pantry')
})

app.listen(PORT, () => {
    console.log('Listening on port', PORT)
})