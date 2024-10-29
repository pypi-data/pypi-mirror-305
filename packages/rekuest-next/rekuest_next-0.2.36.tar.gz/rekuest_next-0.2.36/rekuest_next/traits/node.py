from koil.composition.base import KoiledModel


class Reserve(KoiledModel):

    def validate_args(self, **kwargs):
        for arg in self.args:
            if arg.key not in kwargs and arg.nullable is False:
                raise ValueError(f"Key {arg.key} not in args")

    def get_node_kind(self):
        return getattr(self, "kind")

    async def call_async_func(self, *args, reserve_params={}, **kwargs):
        async with self.reserve(**reserve_params) as res:
            return await res.assign_async(*args, **kwargs)

    async def call_async_gen(self, *args, reserve_params={}, **kwargs):
        async with self.reserve(**reserve_params) as res:
            async for result in res.stream_async(*args, **kwargs):
                yield result

    def __rich_repr__(self):
        yield self.name
        yield "args", self.args
        yield "kwargs", self.kwargs
        yield "returns", self.returns

    def __rich__(self):
        from rich.table import Table

        my_table = Table(title=f"Node: {self.name}", show_header=False)

        my_table.add_row("ID", str(self.id))
        my_table.add_row("Package", self.package)
        my_table.add_row("Interface", self.interface)
        my_table.add_row("Type", self.type)

        return my_table

    def _repr_html_(self):
        return f"""
        <div class="container" style="border:1px solid #00000f;padding: 4px;">
            <div class="item item-1 font-xl">{self.name}</div>
            <div class="item item-2">{self.package}/{self.interface}</div>
            <div class="item item-3">Args:{" ".join([port._repr_html_list() for port in self.args])}
            </div>
            <div class="item item-3">Kwargs: {" ".join([port.key for port in self.kwargs])}</div>
            <div class="item item-3">Returns: {" ".join([port.key for port in self.returns])}</div>
        </div>"""

    async def __aenter__(self):
        from rekuest_next.api.schema import ReserveInput, areserve

        self._reservation = areserve(
            ReserveInput(
                node_reference=self.node_reference,
                kind=self.get_node_kind(),
            )
        )

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        from rekuest_next.api.schema import ReserveInput, UnreserveInput, aunreserve

        if self._reservation:
            await aunreserve(UnreserveInput(reservation=self._reservation))
        return
