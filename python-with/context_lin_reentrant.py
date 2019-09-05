from contextlib import redirect_stdout
from io import StringIO

stream = StringIO()
write_to_stream = redirect_stdout(stream)
with write_to_stream:
    print("This is written to the stream rather than stdout")
    with write_to_stream:
        print("This is also written to the stream")