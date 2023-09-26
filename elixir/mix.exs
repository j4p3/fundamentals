defmodule ElixirImplementations.MixProject do
  use Mix.Project

  def project do
    [
      app: :elixir,
      version: "0.1.0",
      elixir: "~> 1.14",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  # Run "mix help compile.app" to learn about applications.
  def application do
    [
      extra_applications: [:logger]
    ]
  end

  # Run "mix help deps" to learn about dependencies.
  def deps do
    [
      {:ex_doc, "~> 0.21", only: :dev, runtime: false},
      {:benchee, "~> 1.0", only: :dev}
    ]
  end
end
