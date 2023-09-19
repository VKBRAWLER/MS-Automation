This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started
First, install all the dependencies:

```bash
npm i
npm install react-icons --save
npm install express --save
npm install next-auth
npm install mongoose
```

Then, run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.

## Timeline

- Day 1 (29/Aug)
01. Created the app in Next.js and deployed in github.com as [SurveySnap](https://github.com/VKBRAWLER/SurveySnap.git).
02. Emptied the started template and changed the js to jsx for more functionality => (jsx is a mixture of js and html).
- Day 2 (30/Aug)
03. Added react-icon for better user experience.
04. Added Header with static Sign Up button and Navigation bar.
- Day 3 (31/Aug)
05. Added a few images from [Freepik](https://www.freepik.com/) by generating images for HomePage.
06. Used [PhotoShop](https://www.adobe.com/in/products/photoshop.html) to edit the image for better user experience.
- Day 5 (02/Sep)
07. Added HomePage as landing page.
- Day 6 (03/Sep)
08. Added Footer with alias info.
- Day 14 (11/Sep)
09. Added survey page and removed [google fonts](https://fonts.google.com/) from layout.jsx.
- Day 15 (12/Sep)
10. Added demo data for suevey, questions and user.
- Day 16 (13/Sep)
11. Fixed Route rendering by removing it from app/page.jsx to app/layout.jsx.
- Day 19 (16/Sep)
12. Fixed image warning and added dependencies for next-auth and express.
13. Created added session from Provider.jsx to connect authentication routes using client ID from [Google client](https://console.cloud.google.com/).
14. Created database routing from [mongoDB](https://www.mongodb.com/atlas) using mongoose and made schema model in models/user.js using [next-auth](https://next-auth.js.org) and added .env crypto salt using [text-crypto](https://github.com/JeevanJoshi4434/text-crypto).
- Day 20 (17/Sep)
15. Modified Header.jsx to login and use Google Authentication and Callback initiated.
- Day 21 (18/Sep)
16. Modified User Schema to save user information in MongoDB and understood RegExp in Mongoose by posting in [StackOverflow](https://stackoverflow.com/questions/77122094/how-to-use-match-in-schema-while-using-mongoose).
17. Modified survey/id page to create survey.
- Day 22 (19/Sep)
18. Image insertion system added to survey/id.