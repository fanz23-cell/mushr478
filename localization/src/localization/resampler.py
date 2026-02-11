#!/usr/bin/env python3
from __future__ import division

from threading import Lock

import numpy as np


class LowVarianceSampler:
    """Low-variance particle sampler."""

    def __init__(self, particles, weights, state_lock=None):
        """Initialize the particle sampler.

        Args:
            particles: the particles to update
            weights: the weights to update
            state_lock: guarding access to the particles and weights during update,
                since both are shared variables with other processes
        """
        self.particles = particles
        self.weights = weights
        self.state_lock = state_lock or Lock()
        self.n_particles = particles.shape[0]

        # You may want to cache some intermediate variables here for efficiency

    def resample(self):
        """Resample particles using the low-variance sampling scheme.

        Both self.particles and self.weights should be modified in-place.
        """
        # Acquire the lock that synchronizes access to the particles. This is
        # necessary because self.particles is shared by the other particle
        # filter classes.
        #
        # The with statement automatically acquires and releases the lock.
        # See the Python documentation for more information:
        # https://docs.python.org/3/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement
        with self.state_lock:
            # BEGIN QUESTION 3.2
            particles_old = np.copy(self.particles)
            cdf = np.cumsum(self.weights)
            r = np.random.uniform(0.0, 1.0 / self.n_particles)
            new_particles = np.empty_like(self.particles)
            for m in range(self.n_particles):
                u = r + m / self.n_particles
                i = np.searchsorted(cdf, u)
                new_particles[m] = particles_old[i]

            self.particles[:] = new_particles
            self.weights[:] = 1.0 / self.n_particles
            # END QUESTION 3.2
