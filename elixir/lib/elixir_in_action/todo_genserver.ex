defmodule TodoGenserver do
  use GenServer

  defstruct id_sequence: 1, entries: %{}

  @type todo_list :: %{}
  @type entry :: %{date: Date, message: charlist}

  ###################################################################
  # Interface functions
  ###################################################################

  @spec start :: :ignore | {:error, any} | {:ok, pid}
  def start do
    GenServer.start(TodoGenserver, nil, name: __MODULE__)
  end

  @spec create(any) :: any
  def create(entry) do
    GenServer.cast(__MODULE__, {:create, entry})
  end

  @spec update(any, any) :: any
  def update(id, entry) do
    GenServer.cast(__MODULE__, {:update, id, entry})
  end

  @spec delete(any) :: any
  def delete(id) do
    GenServer.cast(__MODULE__, {:delete, id})
  end

  @spec entries(any) :: [TodoGenserver]
  def entries(date) do
    IO.puts("TodoGenserver received entries()")
    GenServer.call(__MODULE__, {:entries, date})
  end

  ###################################################################
  # Callback functions
  ###################################################################

  @impl GenServer
  def init(_), do: {:ok, %TodoGenserver{}}

  @impl GenServer
  # @spec handle_cast(
  #         {:create, map}
  #         | {:delete, any}
  #         | {:update, any, any},
  #         TodoGenserver
  #       ) :: {:noreply, TodoGenserver}
  def handle_cast({:create, entry}, todos) do
    entry = Map.put(entry, :id, todos.id_sequence)

    entries =
      Map.put(
        todos.entries,
        todos.id_sequence,
        entry
      )

    {:noreply,
     %TodoGenserver{
       todos
       | entries: entries,
         id_sequence: todos.id_sequence + 1
     }}
  end

  def handle_cast({:update, id, update_body}, todos) do
    case Map.fetch(todos.entries, id) do
      :error ->
        todos

      {:ok, existing_entry} ->
        new_entry =
          Enum.reduce(
            update_body,
            existing_entry,
            fn {k, v}, acc ->
              %{acc | k => v}
            end
          )

        entries =
          Map.put(
            todos.entries,
            new_entry.id,
            new_entry
          )

        %TodoGenserver{todos | entries: entries}
    end
  end

  def handle_cast({:delete, id}, todos) do
    {_, updated} = Map.pop(todos.entries, id)
    %TodoGenserver{todos | entries: updated}
  end

  @impl GenServer
  # @spec handle_call({:entries, Date}, pid, TodoGenServer):: {:reply, map, TodoGenserver}
  def handle_call({:entries, date}, _caller, todos) do
    IO.puts("TodoGenserver received handle_call()")

    entries =
      todos.entries
      |> Stream.filter(fn {_, entry} -> entry.date == date end)
      |> Enum.map(fn {_, entry} -> entry end)

    {:reply, entries, todos}
  end
end
