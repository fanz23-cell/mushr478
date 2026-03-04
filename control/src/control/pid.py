from __future__ import division
import numpy as np

from control.controller import BaseController
from control.controller import compute_position_in_frame


class PIDController(BaseController):
    def __init__(self, **kwargs):
        self.kp = kwargs.pop("kp")
        self.kd = kwargs.pop("kd")

        # Get the keyword args that we didn't consume with the above initialization
        #super(PIDController, self).__init__(**kwargs)
        # super(PIDController, self).__init__(
        #     **{k: kwargs[k] for k in [
        #         "frequency",
        #         "finish_threshold",
        #         "exceed_threshold",
        #         "distance_lookahead",
        #         "min_speed",
        #     ]}
        # )
        self.__dict__.update({k: kwargs[k] for k in [
            "frequency",
            "finish_threshold",
            "exceed_threshold",
            "distance_lookahead",
            "min_speed",
        ]})

        super(PIDController, self).__init__(
            **{k: kwargs[k] for k in [
                "frequency",
                "finish_threshold",
                "exceed_threshold",
                "distance_lookahead",
                "min_speed",
            ]}
        )


    def get_error(self, pose, reference_xytv):
        """Compute the PD error.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed

        Returns:
            error: across-track and cross-track error
        """

        return compute_position_in_frame(pose, reference_xytv[:3])

    def get_control(self, pose, reference_xytv, error):
        """Compute the PD control law.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed
            error: error vector from get_error

        Returns:
            control: np.array of velocity and steering angle
                (velocity should be copied from reference velocity)
        """
        # BEGIN QUESTION 2.1
        "*** REPLACE THIS LINE ***"
     
        v = reference_xytv[3]

        e_y = error[0]        # cross-track error
        e_theta = error[1]    # heading error

        e_y_dot = v * np.sin(pose[2]-reference_xytv[2])

    # PD control law
        delta = -self.kp * e_theta - self.kd * e_y_dot

        return np.array([v, delta])

        # END QUESTION 2.1
