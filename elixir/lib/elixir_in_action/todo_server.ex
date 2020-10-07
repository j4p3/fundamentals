defmodule TodoOnServer do
  # Step 1: build a functional data structure
  defstruct id_sequence: 1, entries: %{}

  @type todo_list :: %{}
  @type entry :: %{date: Date, message: charlist}

  ###################################################################
  # Interface functions
  ###################################################################

  @spec start :: pid
  def start do
    ServerProcess.start(TodoOnServer)
  end

  @spec create(pid, any) :: any
  def create(pid, entry) do
    ServerProcess.cast(pid, {:create, entry})
  end
  @spec update(pid, any, any) :: any
  def update(pid, id, entry) do
    ServerProcess.cast(pid, {:update, id, entry})
  end
  @spec delete(pid, any) :: any
  def delete(pid, id) do
    ServerProcess.cast(pid, {:delete, id})
  end
  @spec entries(pid, any) :: [TodoOnServer]
  def entries(pid, date) do
    IO.puts("TodoOnServer received entries()")
    ServerProcess.call(pid, {:entries, date})
  end

  ###################################################################
  # Callback functions
  ###################################################################

  def init, do: %TodoOnServer{}

  @spec handle_cast({:create, map} |
  {:delete, any} |
  {:update, any, any}, TodoOnServer) :: atom | %{entries: map}
  def handle_cast({:create, entry}, todos) do
    entry = Map.put(entry, :id, todos.id_sequence)

    entries =
      Map.put(
        todos.entries,
        todos.id_sequence,
        entry
      )

    %TodoOnServer{
      todos
      | entries: entries,
        id_sequence: todos.id_sequence + 1
    }
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

        %TodoOnServer{todos | entries: entries}
    end
  end

  def handle_cast({:delete, id}, todos) do
    {_, updated} = Map.pop(todos.entries, id)
    %TodoOnServer{todos | entries: updated}
  end

  def handle_call({:entries, date}, todos) do
    IO.puts("TodoOnServer received handle_call()")
    entries = todos.entries
    |> Stream.filter(fn {_, entry} -> entry.date == date end)
    |> Enum.map(fn {_, entry} -> entry end)
    {entries, todos}
  end
end
