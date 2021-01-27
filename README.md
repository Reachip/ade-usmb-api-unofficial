# ADE USMB API

This is the source code of a non-official REST API about timetables of some departements and team-work in the University of Savoie Mont Blanc. 

The aim of this project is to purpose a simple way to fetch data about timetables of the university to thruster new projects about it. 


# Contributing

- Fork the repo on GitHub
- Clone the project to your own machine
- Commit changes to your own branch
- Push your work back up to your fork
- Submit a Pull request

## Work locally

By constraint, the API work with some ICS files located on the folder called "ics". You should take this files on <https://ade6-usmb-ro.grenet.fr> to deal with API.

**NB:** This service will soon be hosted on a server. At this point you will have to recover the files yourself only if you want to contribute.

# Documentation

## Endpoint

```
/api/<departement>/<team work>
```


## List of team work timetables according to departement

| Departement        | team work           | 
| -------------      |--------------       |
| info1              | 11, 12, 13, 14, 15  | 
| gmp1               | a1, a2, b1, b2, c1, c2 |  


## Example

```bash
curl http://localhost/api/info1/11
```
```js
{
  "code": 200,
  "response": [
    {
      "begin": "2021-05-12 14:00:00+00:00",
      "end": "2021-05-12 16:00:00+00:00",
      "room": "D360 (16 pl.)",
      "subject": "M2105-TD1A-BD"
    },
    {
      "begin": "2021-04-28 10:00:00+00:00",
      "end": "2021-04-28 11:00:00+00:00",
      "room": "A252 (86pl.masque)",
      "subject": "M2203-soutien-YG"
    },
    {
      "begin": "2021-05-10 12:00:00+00:00",
      "end": "2021-05-10 14:00:00+00:00",
      "room": "D353 (12 pl.)",
      "subject": "M2104-TP11-2-NG"
    },

    // etc.
}
```

