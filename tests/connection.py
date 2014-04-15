from spec import Spec, skip, eq_

from fabric import Connection


class Connection_(Spec):
    class init:
        "__init__"

        def host_required(self):
            skip()

        def user_defaults_to_local_user(self):
            skip()

        def user_may_be_given_explicitly(self):
            skip()

        def port_defaults_to_22(self):
            # TODO: default to a configured value
            skip()

        def port_may_be_given_explicitly(self):
            skip()

    class run:
        # uses invoke.runner.run() with runner=fabric.runners.Remote
        pass

    class sudo:
        # uses runner=fabric.runners.RemoteSudo
        pass

    class put:
        # fabric1's put() copied?
        pass

    class get:
        # ditto
        pass
