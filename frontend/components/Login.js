import React from 'react'
import { useHistory, Link } from 'react-router-dom'
import { useForm } from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers'
import * as Yup from 'yup'
import axios from 'axios'
import { login } from '../lib/auth'
import FadeIn from 'react-fade-in'
import splashLogo from '../assets/pav-logo.png'

const loginSchema = Yup.object().shape({
  email: Yup.string()
    .required('No email provided'),
  password: Yup.string()
    .required('Please enter a password')
    .matches(
      /^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{7,})\S$/,
      'Must Contain 8 Characters, one uppercase, one lowercase and one number'
    )
})

export const Login = () => {

  const history = useHistory()
  const { register, handleSubmit, errors, setError } = useForm({
    resolver: yupResolver(loginSchema),
    criteriaMode: 'all'
  })

  const onSubmit = values => {
    axios.post('/api/login', values)
      .then(resp => {

        login(resp.data.token)
        console.log(resp.data)
        history.push('/pavlova')
      })
      .catch(err => {
        console.log(err.response)
        const errorMessages = {
          email: 'Email address not found',
          password: 'Incorrect password'
        }
        Object.keys(err.response.data).forEach(errorField => {
          setError(errorField, { message: `${errorMessages[errorField]}` })
        })
      })
  }

  return (
    <section id="login">
      <FadeIn>
        <h1>Welcome Back</h1>
        <img src={splashLogo} />
        <form onSubmit={handleSubmit(onSubmit)}>
          <label htmlFor="email">Enter email</label><br></br>
          <input id="email" type="emai" name="email" autoComplete="off" placeholder="Email address" ref={register} />
          <p>{errors.email?.message}</p>
          <label htmlFor="password">Enter your password</label><br></br>
          <input id="password" type="password" name="password" autoComplete="off" placeholder="Password" ref={register} />
          <p>{errors.password?.message}</p>
          <button type="submit">➜</button>
          <Link to="/register">
            <h4>{"Don't have an account yet? Sign up!"}</h4>
          </Link>
        </form>

      </FadeIn>
    </section>
  )
}