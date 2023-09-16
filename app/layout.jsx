import './globals.css';
import Header from '@components/Header';
import Footer from '@components/Footer';
import Provider from '@components/Provider';
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Provider>
          <Header/>
          {children}
          <Footer/>
        </Provider>
        </body>
    </html>
  )
}
